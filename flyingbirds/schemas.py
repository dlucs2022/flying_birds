'''




与模型相对应的类   集成basemodel  响应前端

'''

from datetime import datetime
from datetime import date as date_
from pydantic import BaseModel
from sqlalchemy import Time
from datetime import date, time
from typing import List
from fastapi import File, UploadFile


class CreateBirdData(BaseModel):
    '''
    三个表共有数据
    '''
    device_name: str
    time: date
    satellites: int
    speed: str
    altitude: str
    longitude: str
    latitude: str
    species: str = 'default_species'


class ReadBirdData(CreateBirdData):
    '''
    三个表共有数据
    '''

    class Config:
        orm_model = True


class CreateSpeciesData(BaseModel):
    '''
    三个表共有数据
    '''

    species: str = None


class ReadSpeciesData(CreateSpeciesData):
    '''
    三个表共有数据
    '''

    class Config:
        orm_model = True


class CreateData(BaseModel):
    '''
    d单个表数据------3

    '''
    x_id: str
    device_id: str
    data_format: str
    longitude: str
    latitude: str
    n_s_Latitude: str
    e_w_longitude: str
    date1: str
    time1: str
    height: str
    speed: str
    azimuth: str
    temperature: str
    voltage: str
    c_s_level: str
    x2d_3d: str
    pdop: str
    hdop: str
    x_axis_angle: str
    y_axis_angle: str
    z_axis_angle: str
    species: str = 'default_species'


class ReadData(CreateData):
    '''
    d单个表数据-----   3

    '''
    id: int

    class Config:
        orm_model = True


class CreateData1(BaseModel):
    '''
    个表共有数据   ------1
    '''
    terminal_id: str
    imei_id: str
    timestamp: str
    object_name: str
    longitude: str
    north_south: str
    latitude: str
    speed: str
    heading: str
    altitude: str
    temperature: str
    voltage: str
    motion: str
    satellites: int
    hdop: str
    vdop: str
    accuracy: str
    validity: str
    species: str = 'default_species'


class ReadData1(CreateData1):
    '''
    d单个表数据0----------1

    '''
    id: int

    class Config:
        orm_model = True


class CreateData2(BaseModel):
    '''
    GPS 数据表    ---------2
    '''
    uuid: str
    transmitting_time: str
    collecting_time: str
    longitude: str
    latitude: str
    altitude: str
    altitude_ellipsoid: str
    speed: str
    ned_speed: str
    course: str
    satellite_used: str
    positioning_mode: str
    hor_accuracy: str
    ver_accuracy: str
    gps_time_consumption: str
    data_source: str
    hdop: str
    vdop: str
    species: str = 'default_species'


class ReadData2(CreateData2):
    '''
    d单个表数据-------------2

    '''
    id: int

    class Config:
        orm_model = True


class FileUpload(BaseModel):
    files: List[UploadFile] = File(...)
