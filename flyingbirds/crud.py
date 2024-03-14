'''


对数据库的操作，增删改差


'''

from sqlalchemy.orm import Session
from flyingbirds import model, schemas



def create_data(db: Session, data1: list,species1:str):
    created_objects = []

    for data_ in data1:
        data_['species'] = species1
        db_data = model.Brid_data(**data_)
        db.add(db_data)
    db.commit()  # 提交每个对象的变化
    created_objects.append(db_data)  # 将创建的对象添加到列表中
    return created_objects  # 返回所有创建的对象

#第三个单独表
def create_data_fist1(db: Session, data1: list,species1:str):
    created_objects = []
    for data_ in data1:
        data_['species'] = species1
        db_data = model.Brid_data1(**data_)
        db.add(db_data)
    db.commit()  # 提交每个对象的变化
    db.refresh(db_data)  # 刷新对象以确保获取数据库生成的ID等信息
    created_objects.append(db_data)  # 将创建的对象添加到列表中
    return created_objects  # 返回所有创建的对象
#第1个单独的表
def create_data_fist2(db: Session, data1: list,species1:str):
    created_objects = []
    for data_ in data1:
        data_['species'] = species1
        db_data = model.Brid_data2(**data_)
        db.add(db_data)
    db.commit()  # 提交每个对象的变化
    db.refresh(db_data)  # 刷新对象以确保获取数据库生成的ID等信息
    created_objects.append(db_data)  # 将创建的对象添加到列表中
    return created_objects  # 返回所有创建的对象

#第2个单独的表
def create_data_fist3(db: Session, data1: list,species1:str):
    created_objects = []
    for data_ in data1:
        data_['species'] = species1
        db_data = model.Brid_data3(**data_)
        db.add(db_data)
    db.commit()  # 提交每个对象的变化
    db.refresh(db_data)  # 刷新对象以确保获取数据库生成的ID等信息
    created_objects.append(db_data)  # 将创建的对象添加到列表中
    return created_objects  # 返回所有创建的对象


