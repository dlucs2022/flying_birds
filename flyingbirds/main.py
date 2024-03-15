'''


应用的逻辑
'''

import os.path
from typing import List

from fastapi import APIRouter, dependencies, HTTPException, status, Request, Depends, Form
from sqlalchemy.orm import Session
from flyingbirds import crud, schemas
from flyingbirds.alone_create import create_data3, create_data2, create_data1
from flyingbirds.database import engine, Base, sessionLocal

from fastapi import File, UploadFile

from flyingbirds.file_extension import is_csv
from flyingbirds.model import Species
from flyingbirds.schemas import CreateData, CreateData1, CreateData2
from paser_data.other import get_data_json, get_file_type

application = APIRouter()
Base.metadata.create_all(bind=engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



@application.post('/upload')
async def create_data(species: str = Form(..., description="物种名称"), files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    """

    :param files:
    :param db:
    :return:
    """
    success_count = 0  # 计数器，记录成功传输的文件夹数目
    for file in files:
        if is_csv(file.filename):
            # 将上传的文件保存到服务器上的指定路径
            with open(os.path.join(r"upload", file.filename), 'wb') as f:
                content = await file.read()
                f.write(content)
            # 记录物种数据写入数据库
            new_species = Species(species=species)
            crud.create_species_data(db=db, data1=new_species)
            # 解析上传文件的数据
            dataunion = get_data_json(os.path.join(r"upload", file.filename))

            # 将解析后的数据存储到数据库中
            crud.create_data(db=db, data1=dataunion, species_id=new_species.id)

            # 单个文件判断文件类型：
            file_type = get_file_type(os.path.join(r"upload", file.filename))
            if file_type == 1:
                create_data3(file, db, species)
            elif file_type == 2:
                create_data2(file, db, species)
            elif file_type == 3:
                create_data1(file, db, species)
            else:
                print('输入是新数据')
            # 每成功传输一个文件夹，计数器加一
            success_count += 1
    if success_count > 0:
        return {'msg': '数据传输成功{}个文件夹'.format(success_count)}
    else:
        return {'msg': '没有传输任何数据'}


@application.post('/query_species')
async def query_species(species: str = Form(..., description="物种名称"),skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    speciesid = crud.get_species_id(db=db, species_name=species)
    if speciesid:
        return crud.get_common_data(db=db, id_species=speciesid,skip=skip,limit=limit)
    else:
        return "{'msg': '没有该物种'}"
