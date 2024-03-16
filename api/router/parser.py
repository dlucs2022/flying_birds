import hashlib
import os.path
from datetime import datetime
from typing import List, Optional

from fastapi import Form, UploadFile, File, status, Query
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from api.utils.save_data import save_data
from database.database import SESSION_LOCAL
from database.tables import BirdSpecies, BirdCommonData
from model.model import BirdCommonData as BirdCommonDataModel

from parse_data import parse_common_data
from config import CACHE_DIR

parser_router = APIRouter()

@parser_router.post("/parser", summary="解析数据")
async def parser_api(  # TODO: 解决数据重复问题
    files: List[UploadFile] = File(..., description="csv文件"),
    species: str = Form(..., description="鸟类种类"),
    encoding: str = Form("gb2312", description="编码格式:如果失败utf-8/gbk"),
):
    """
    # 解析数据
    ## 参数
    - `files`: csv文件, binary, required
    - `species`: 鸟类种类, string, required
    - `encoding`: 编码格式, string, default: "gb2312"
    """
    with SESSION_LOCAL() as session:
        for file in files:
            file_data = await file.read()
            file_path = os.path.join(CACHE_DIR, file.filename)
            with open(file_path, "wb") as f:
                f.write(file_data)

          #判断编码类型，进行解析
            try:
                data = parse_common_data(file_path, encoding)
            except UnicodeDecodeError:
                # 如果在初始编码下解析时发生UnicodeDecodeError，尝试另一种编码
                alternative_encoding = "utf-8"  # 使用备用编码重新尝试
                data = parse_common_data(file_path, alternative_encoding)

            # 获取鸟类物种
            species_record = (
                session.query(BirdSpecies).filter(BirdSpecies.name == species).first()
            )
            if not species_record:
                species_record = BirdSpecies(name=species)
                session.add(species_record)
                session.flush()
                session.commit()
                session.refresh(species_record)

            # save data to database
            save_data(data, species_record, session)

        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"code": 0, "message": "success"}
        )


@parser_router.get("/data", summary="解析数据")
async def get_data_api(
    species: Optional[str] = Query(None, description="鸟类种类"),
    page: int = Query(1, description="页码"),
    page_size: int = Query(10, description="每页数量"),
    order_by: str = Query("create_time", description="排序字段"),
    order: str = Query("desc", description="排序方式"),
):

    with SESSION_LOCAL() as session:
        query = session.query(BirdCommonData)
        if species:
            query = query.join(BirdSpecies).filter(BirdSpecies.name == species)
        assert order_by in BirdCommonData.__dict__, ValueError("排序字段不存在")
        total = query.count()
        total_page = (total + page_size - 1) // page_size
        data = (
            query.order_by(
                BirdCommonData.__dict__[order_by]
                if order == "asc"
                else BirdCommonData.__dict__[order_by].desc()
            )
            .limit(page_size)
            .offset((page - 1) * page_size)
            .all()
        )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "code": 0,
                "message": "success",
                "data": [
                    BirdCommonDataModel.model_validate(data).model_dump()
                    for data in data
                ],
                "total": total,
                "total_page": total_page,
                "current_page": page,
                "page_size": page_size,
                "order_by": order_by,
                "order": order,
            },
        )


@parser_router.get("/species", summary="获取鸟类种类")
async def get_species_api():
    with SESSION_LOCAL() as session:
        species = session.query(BirdSpecies).all()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "code": 0,
                "message": "success",
                "data": [species.name for species in species],
            },
        )
