
import csv
import os.path
from flyingbirds import crud, schemas
from flyingbirds.schemas import CreateData ,CreateData1,CreateData2

# 创建第一个单独文件夹kiz账户5只个体.csv
def create_data1(file, db, species):
    json_data = []
    with open(os.path.join(r"upload", file.filename), "r", encoding="gbk") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # 跳过表头
        for line in csvreader:
            row_dict = {
                'x_id': line[0],
                'device_id': line[1],
                'data_format': line[2],
                'longitude': line[3],
                'latitude': line[4],
                'n_s_Latitude': line[5],
                'e_w_longitude': line[6],
                'date1': line[7],
                'time1': line[8],
                'height': line[9],
                'speed': line[10],
                'azimuth': line[11],
                'temperature': line[12],
                'voltage': line[13],
                'c_s_level': line[14],
                'x2d_3d': line[15],
                'pdop': line[16],
                'hdop': line[17],
                'x_axis_angle': line[18],
                'y_axis_angle': line[19],
                'z_axis_angle': line[20]
            }
            row = CreateData(**row_dict)
            json_data.append(row.dict())
    crud.create_data_fist1(db=db, data1=json_data, species1=species)


# 第二个表的导入数据库"['UUID', 'Transmitting.time', 'Collecting.time', 'Longitude', 'Latitude', 'Altitude', 'Altitude..Ellipsoid.', 'Speed', 'NED.Speed', 'Course', 'Satellite.used', 'Positioning.mode', 'HorAccuracy', 'VerAccuracy', 'GPS.time.consumption', 'Data.Source', 'HDOP', 'VDOP']":2,
# 创建第一个单独文件夹kiz账户5只个体.csv
def create_data2(file, db, species):
    json_data = []
    with open(os.path.join(r"upload", file.filename), "r", encoding="gbk") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # 跳过表头
        for line in csvreader:
            row_dict = {
                'uuid': line[0],
                'transmitting_time': line[1],
                'collecting_time': line[2],
                'longitude': line[3],
                'latitude': line[4],
                'altitude': line[5],
                'altitude_ellipsoid': line[6],
                'speed': line[7],
                'ned_speed': line[8],
                'course': line[9],
                'satellite_used': line[10],
                'positioning_mode': line[11],
                'hor_accuracy': line[12],
                'ver_accuracy': line[13],
                'gps_time_consumption': line[14],
                'data_source': line[15],
                'hdop': line[16],
                'vdop': line[17]
            }
            row = CreateData2(**row_dict)
            json_data.append(row.dict())
    crud.create_data_fist3(db=db, data1=json_data, species1=species)






# #第三个表格的导入数据库"['X.U.FEFF.终端', 'IMEID', '时间', '东西', '经度', '南北', '纬度', '速度', '航向', '高度', '温度', '电压', '运动量', '卫星', 'HDOP', 'VDOP', '精度', '有效性']":1,
#                     "":2,
# 创建第一个单独文件夹kiz账户5只个体.csv
def create_data3(file, db, species):
    json_data = []
    with open(os.path.join(r"upload", file.filename), "r", encoding="gbk") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # 跳过表头
        for line in csvreader:
            row_dict = {
                'terminal_id': line[0],
                'imei_id': line[1],
                'timestamp': line[2],
                'object_name': line[3],
                'longitude': line[4],
                'north_south': line[5],
                'latitude': line[6],
                'speed': line[7],
                'heading': line[8],
                'altitude': line[9],
                'temperature': line[10],
                'voltage': line[11],
                'motion': line[12],
                'satellites': line[13],
                'hdop': line[14],
                'vdop': line[15],
                'accuracy': line[16],
                'validity': line[17]
            }
            row = CreateData1(**row_dict)
            json_data.append(row.dict())
    crud.create_data_fist2(db=db, data1=json_data, species1=species)

