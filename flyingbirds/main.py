'''


应用的逻辑
'''
import asyncio
import csv
import os.path
from typing import List

import aiofiles
from fastapi import APIRouter, dependencies, HTTPException, status, Request, Depends
from sqlalchemy.orm import Session
from flyingbirds import crud, schemas
from flyingbirds.alone_create import create_data3, create_data2, create_data1
from flyingbirds.database import engine, Base, sessionLocal

from fastapi import File, UploadFile

from flyingbirds.schemas import CreateData ,CreateData1,CreateData2
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
async def create_data(species: str, files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    """

    :param files:
    :param db:
    :return:
    """
    success_count = 0  # 计数器，记录成功传输的文件夹数目
    for file in files:
        # 将上传的文件保存到服务器上的指定路径
        with open(os.path.join(r"upload", file.filename), 'wb') as f:
            content = await file.read()
            f.write(content)
        # 解析上传文件的数据
        dataunion = get_data_json(os.path.join(r"upload", file.filename))

        # 将解析后的数据存储到数据库中
        crud.create_data(db=db, data1=dataunion, species1=species)

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
async def query_species(species: str, files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    pass
