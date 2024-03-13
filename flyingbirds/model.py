import csv
from sqlalchemy import Column, String, Integer, BigInteger, Date, ForeignKey, func, DateTime, Text, Time
from .database import Base
import psycopg2


# 从 CSV 文件中读取列名['X.U.FEFF.编号', '设备号', '数据格式', '经度', '纬度', '南北纬', '东西经', '日期',
# '时间', '高度', '速度', '方位角', '温度', '电压', '通信信号等级', 'X2D.3D', 'PDOP', 'HDOP', 'X轴角度', 'Y轴角度', 'Z轴角度']
# ['ID', 'Device ID', 'Data Format', 'Longitude', 'Latitude', 'North/South Latitude', 'East/West Longitude', 'Date', 'Time',
#  'Height', 'Speed', 'Azimuth', 'Temperature', 'Voltage', 'Communication Signal Level', 'X2D_3D', 'PDOP', 'HDOP', 'X-axis Angle', 'Y-axis Angle', 'Z-axis Angle']
# ['id', 'device id', 'data format', 'longitude', 'latitude', 'north/south latitude', 'east/west longitude', 'date', 'time',
# 'height', 'speed', 'azimuth', 'temperature', 'voltage', 'communication signal level', 'x2d_3d', 'pdop', 'hdop', 'x-axis angle', 'y-axis angle', 'z-axis angle']
class Brid_data(Base):
    '''

    三个表共有字段

    '''
    __tablename__ = 'Brid_data'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    device_name = Column(String(100), nullable=True, comment='设备号')
    time = Column(String(100), nullable=True, comment='时间')
    satellites = Column(Integer, nullable=True, comment='卫星数')
    speed = Column(String(100), nullable=True, comment='速度')
    altitude = Column(String(100), nullable=True, comment='高度')
    longitude = Column(String(100), nullable=True, comment='温度')
    latitude = Column(String(100), nullable=True, comment='电压')
    species = Column(String(100), nullable=True, comment='物种')

    def __repr__(self):
        return f'这是Brid_data_union'


class Brid_data1(Base):
    '''

    单个表共有字段  第三个

    '''
    __tablename__ = 'Brid_data1'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    x_id = Column(String(100), nullable=True, comment='编号')
    device_id = Column(String(100), nullable=True, comment='设备号')
    data_format = Column(String(100), nullable=True, comment='数据格式')
    longitude = Column(String(100), nullable=True, comment='经度')
    latitude = Column(String(100), nullable=True, comment='纬度')
    n_s_Latitude = Column(String(100), nullable=True, comment='南北纬')
    e_w_longitude = Column(String(100), nullable=True, comment='东西经')
    date1 = Column(String(100), nullable=True, comment='日期')
    time1 = Column(String(100), nullable=True, comment='时间')
    height = Column(String(100), nullable=True, comment='高度')
    speed = Column(String(100), nullable=True, comment='速度')
    azimuth = Column(String(100), nullable=True, comment='方位角')
    temperature = Column(String(100), nullable=True, comment='温度')
    voltage = Column(String(100), nullable=True, comment='电压')
    c_s_level = Column(String(100), nullable=True, comment='通信信号等级')
    x2d_3d = Column(String(100), nullable=True, comment='X2D')
    pdop = Column(String(100), nullable=True, comment='PDOP')
    hdop = Column(String(100), nullable=True, comment='HDOP')
    x_axis_angle = Column(String(100), nullable=True, comment='X轴角度')
    y_axis_angle = Column(String(100), nullable=True, comment='Y轴角度')
    z_axis_angle = Column(String(100), nullable=True, comment='Z轴角度')
    species = Column(String(100), nullable=True, comment='物种')

    def __repr__(self):
        return f'这是Brid_data1'
    
    
    


class Brid_data2(Base):
    '''
    GPS 数据表
    '''
    __tablename__ = 'Brid_data2'

    id = Column(Integer, primary_key=True, autoincrement=True)
    terminal_id = Column(String(100))
    imei_id = Column(String(100))
    timestamp = Column(String(100))
    object_name = Column(String(100))
    longitude = Column(String(100))
    north_south = Column(String(100))
    latitude = Column(String(100))
    speed = Column(String(100))
    heading = Column(String(100))
    altitude = Column(String(100))
    temperature = Column(String(100))
    voltage = Column(String(100))
    motion = Column(String(100))
    satellites = Column(Integer)
    hdop = Column(String(100))
    vdop = Column(String(100))
    accuracy = Column(String(100))
    validity = Column(String(100))
    species = Column(String(100), nullable=True, comment='物种')

    def __repr__(self):
        return f'<GPSData(id={self.id}, terminal_id={self.terminal_id}, imei_id={self.imei_id}, timestamp={self.timestamp}, ...)>'


class Brid_data3(Base):
    '''
    GPS 数据表
    '''
    __tablename__ = 'Brid_data3'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(100))
    transmitting_time = Column(String(100))
    collecting_time = Column(String(100))
    longitude = Column(String(100))
    latitude = Column(String(100))
    altitude = Column(String(100))
    altitude_ellipsoid = Column(String(100))
    speed = Column(String(100))
    ned_speed = Column(String(100))
    course = Column(String(100))
    satellite_used = Column(String(100))
    positioning_mode = Column(String(100))
    hor_accuracy = Column(String(100))
    ver_accuracy = Column(String(100))
    gps_time_consumption = Column(String(100))
    data_source = Column(String(100))
    hdop = Column(String(100))
    vdop = Column(String(100))
    species = Column(String(100), nullable=True, comment='物种')


    def __repr__(self):
        return f'<GPSData(id={self.id}, uuid={self.uuid}, transmitting_time={self.transmitting_time}, ...)>'