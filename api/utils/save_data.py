from api.utils.get_unique import get_unique_value
from database.tables import BirdCommonData
from datetime import datetime
from sqlalchemy.dialects.postgresql import insert


def save_data(data, species_record, session):
    objects = []
    for index, item in enumerate(data):
        unique_value = get_unique_value(*list(item.values()))
        bird_common_data = BirdCommonData(
            device_name=str(item.get("device_name")),
            time=(
                datetime.strptime(item.get("time"), "%Y-%m-%d %H:%M:%S")
                if item.get("time")
                else None
            ),
            satellites=int(item.get("satellites")),
            speed=float(item.get("speed")),
            altitude=float(item.get("altitude")),
            longitude=float(item.get("longitude")),
            latitude=float(item.get("latitude")),
            species_id=species_record.id,
            unique=get_unique_value(*list(item.values())),
        )
        bird_common_data=bird_common_data.__dict__
        bird_common_data.pop("_sa_instance_state")
        objects.append(bird_common_data)
        if (index + 1) % 2000 == 0:
            stmt = insert(BirdCommonData).values(
                objects
            ).on_conflict_do_nothing(index_elements=['unique'])  # 指定unique列为唯一约束基础
            session.execute(stmt)
            session.commit()
            objects = []
    if len(objects)>=1:
        stmt = insert(BirdCommonData).values(
            objects
        ).on_conflict_do_nothing(index_elements=['unique'])  # 指定unique列为唯一约束基础

        session.execute(stmt)
        session.commit()

# def save_data(data,species_record,session):
# objects = []
# unique_values_set = set()  # 用于存储当前批次中所有记录的 unique 值
# for index, item in enumerate(data):
#     # 检测是否存在相同的unique
#     unique_value = get_unique_value(*list(item.values()))
#     # 检查 objects 列表中是否已存在该 "unique" 值的记录
#     if unique_value in unique_values_set:
#         continue  # 如果找到重复的 "unique" 值，跳过这条记录
#     unique_values_set.add(unique_value)
#     existing_record = session.query(BirdCommonData).filter(BirdCommonData.unique == unique_value).first()
#     if existing_record:
#         continue  # 如果记录已存在，跳过插入
#
#     item: dict
#     objects.append(
#         BirdCommonData(
#             device_name=str(item.get("device_name")),
#             time=(
#                 datetime.strptime(item.get("time"), "%Y-%m-%d %H:%M:%S")
#                 if item.get("time")
#                 else None
#             ),
#             satellites=int(item.get("satellites")),
#             speed=float(item.get("speed")),
#             altitude=float(item.get("altitude")),
#             longitude=float(item.get("longitude")),
#             latitude=float(item.get("latitude")),
#             species_id=species_record.id,
#             unique=get_unique_value(*list(item.values())),
#         )
#     )
#
#     if (index + 1) % 2000 == 0:
#         session.bulk_save_objects(
#             objects,
#         )
#         session.commit()
#         objects = []
# session.bulk_save_objects(
#     objects,
# )
# session.commit()
