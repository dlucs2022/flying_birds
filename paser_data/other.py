# 测试代码
import pandas as pd
from datetime import datetime
import json

from paser_data.machine01 import Machine01
from paser_data.machine02 import Machine02
from paser_data.machine03 import Machine03

# file_path = r'C:\Users\squir\Desktop\杨导开发任务\赤麻鸭-剑湖-5只-湖南1.csv'
file_path = r'../kiz账户5只个体.csv'
# file_path = r'C:\Users\squir\Desktop\杨导开发任务\kiz账户5只个体.csv'


fileHead_class_dict = {"['X.U.FEFF.终端', 'IMEID', '时间', '东西', '经度', '南北', '纬度', '速度', '航向', '高度', '温度', '电压', '运动量', '卫星', 'HDOP', 'VDOP', '精度', '有效性']":1,
                    "['UUID', 'Transmitting.time', 'Collecting.time', 'Longitude', 'Latitude', 'Altitude', 'Altitude..Ellipsoid.', 'Speed', 'NED.Speed', 'Course', 'Satellite.used', 'Positioning.mode', 'HorAccuracy', 'VerAccuracy', 'GPS.time.consumption', 'Data.Source', 'HDOP', 'VDOP']":2,
                   "['X.U.FEFF.编号', '设备号', '数据格式', '经度', '纬度', '南北纬', '东西经', '日期', '时间', '高度', '速度', '方位角', '温度', '电压', '通信信号等级', 'X2D.3D', 'PDOP', 'HDOP', 'X轴角度', 'Y轴角度', 'Z轴角度']":3}
'''
    以csv文件表头作为键，类为值
    1表示machine01来接收文件
    目前仅有3类csv文件分别对应三个类
'''

def get_file_type(file_path):
    # 使用pandas读取表头信息转为列表再转为字符串，用作查找文件类型的键值
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='gbk')
    except FileNotFoundError:
        print("文件不存在！")
    except PermissionError:
        print("没有权限打开文件！")
    except IsADirectoryError:
        print("该路径是一个目录！")
    except FileExistsError:
        print("文件已经存在！")
    except OSError as e:
        print(f"发生了文件操作相关的错误：{e}")

    head = df.columns.tolist()
    str01 = str(head)
    # print(str01)
    return fileHead_class_dict[str01]

# print(get_file_type(file_path))

def get_data_json(file_path):
    '''
    调用次方法解析CSV文件
    :param file_path: 待解析csv文件的路径
    :return:没有返回值，但是会在当前目录下创建一个json文件，文件名称为：data_年月日时分秒.json
            例如：data_2024_03_12_16_38_02.json
    '''
    file_type = get_file_type(file_path)

    # 读取 CSV 文件
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='gbk')
    except FileNotFoundError:
        print("文件不存在！")
    except PermissionError:
        print("没有权限打开文件！")
    except IsADirectoryError:
        print("该路径是一个目录！")
    except FileExistsError:
        print("文件已经存在！")
    except OSError as e:
        print(f"发生了文件操作相关的错误：{e}")

    # 初始化一个空的对象列表
    data_list = []

    # i = 1
    # 遍历CSV数据，创建对象并添加到列表中
    for index, row in df.iterrows():
        # i += 1
        # print("下面是第"+str(i)+"行数据")
        row_values = row.values
        if(file_type == 1):
            data_obj = Machine01(*row_values)  # 为每一行数据创建一个对象
        elif(file_type == 2):
            data_obj = Machine02(*row_values)  # 为每一行数据创建一个对象
        elif(file_type == 3):
            data_obj = Machine03(*row_values)  # 为每一行数据创建一个对象
        else:
            print("输入的文件是新的类型，请添加新的类")

        # 按行将数据存储到列表中
        data_list.append(data_obj.get_public_properties())

    '''
    
    # 获取当前时间
    # current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # # 构建带有时间戳的 JSON 文件名
    # json_file_path = f"data_{current_time}.json"
    #
    # # 将字典列表存储为 JSON 文件
    # with open(json_file_path, "w") as json_file:
    #     json.dump(data_list, json_file)
    #
    # print(f"数据已保存到 {json_file_path} 文件中.")
    '''

    return data_list


