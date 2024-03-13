'''


对数据库的操作，增删改差


'''

from sqlalchemy.orm import Session, joinedload, selectinload
from flyingbirds import model, schemas


def create_data(db: Session, data1: list, species_id: int):
    created_objects = []

    for data_ in data1:
        data_['species_id'] = species_id
        db_data = model.BirdCommon(**data_)
        db.add(db_data)
    db.commit()  # 提交每个对象的变化
    created_objects.append(db_data)  # 将创建的对象添加到列表中
    return created_objects  # 返回所有创建的对象


# 创建写入物种表类
def create_species_data(db: Session, data1: schemas.CreateSpeciesData):
    # db_data = model.Species(**data1)
    db.add(data1)
    db.commit()  # 提交每个对象的变化
    return data1  # 返回所有创建的对象


# 第三个单独表
def create_data_fist1(db: Session, data1: list, species1: str):
    created_objects = []
    for data_ in data1:
        data_['species'] = species1
        db_data = model.BirdData1(**data_)
        db.add(db_data)
    db.commit()  # 提交每个对象的变化
    db.refresh(db_data)  # 刷新对象以确保获取数据库生成的ID等信息
    created_objects.append(db_data)  # 将创建的对象添加到列表中
    return created_objects  # 返回所有创建的对象


# 第1个单独的表
def create_data_fist2(db: Session, data1: list, species1: str):
    created_objects = []
    for data_ in data1:
        data_['species'] = species1
        db_data = model.BirdData2(**data_)
        db.add(db_data)
    db.commit()  # 提交每个对象的变化
    db.refresh(db_data)  # 刷新对象以确保获取数据库生成的ID等信息
    created_objects.append(db_data)  # 将创建的对象添加到列表中
    return created_objects  # 返回所有创建的对象


# 第2个单独的表
def create_data_fist3(db: Session, data1: list, species1: str):
    created_objects = []
    for data_ in data1:
        data_['species'] = species1
        db_data = model.BirdData3(**data_)
        db.add(db_data)
    db.commit()  # 提交每个对象的变化
    db.refresh(db_data)  # 刷新对象以确保获取数据库生成的ID等信息
    created_objects.append(db_data)  # 将创建的对象添加到列表中
    return created_objects  # 返回所有创建的对象


def get_species_id(db: Session, species_name: str):
    result = db.query(model.Species.id).filter(model.Species.species == species_name).first()
    if result:
        return result[0]  # result 是一个包含查询结果列的元组，这里只查询了id，所以直接返回result[0]
    else:
        return None  # 如果没有找到对应的物种，返回None


def get_common_data(db: Session, id_species: int,skip:int=0 ,limit:int=10):
    return db.query(model.BirdCommon)\
        .filter(model.BirdCommon.species_id == id_species)\
        .options(selectinload(model.BirdCommon.species))\
        .offset(skip)\
        .limit(limit)\
        .all()
    # return db.query(model.BirdCommon).filter(model.BirdCommon.species.has(id=id_species)).all()
