# ID:1211-赤麻鸭雄鸟剑湖20210123
from trans.device import Device
import re
from datetime import datetime

class Machine03(Device):
    def __init__(self, X_U_FEFF_Number,Device_No,Data_Format,Longitude,Latitude,
                 North_south,Eastern_Western,Date,Time,Altitude,
                 Speed,Azimuth,Temperature,Voltage,Communication_signal_level,
                 X2D_3D,PDOP,HDOP,X_axis_angle,Y_axis_angle,
                 Z_axis_angle):
        '''
        对象参数和CSV文件表头对应关系
        :param X_U_FEFF_Number: X.U.FEFF.编号
        :param Device_No:设备号
        :param Data_Format:数据格式
        :param Longitude:经度
        :param Latitude:纬度
        :param North_south:南北纬
        :param Eastern_Western:东西经
        :param Date:日期
        :param Time:时间
        :param Altitude:高度
        :param Speed:速度
        :param Azimuth:方位角
        :param Temperature:温度
        :param Voltage:电压
        :param Communication_signal_level:通信信号等级
        :param X2D_3D: X2D.3D
        :param PDOP:PDOP
        :param HDOP:HDOP
        :param X_axis_angle:X轴角度
        :param Y_axis_angle:Y轴角度
        :param Z_axis_angle:Z轴角度
        '''
        self._X_U_FEFF_Number = X_U_FEFF_Number
        self._Device_No = Device_No
        self._Data_Format = Data_Format
        self._Longitude = Longitude
        self._Latitude = Latitude
        self._North_south = North_south
        self._Eastern_Western = Eastern_Western
        self._Date = Date
        self._Time = Time
        self._Altitude = Altitude
        self._Speed = Speed
        self._Azimuth = Azimuth
        self._Temperature = Temperature
        self._Voltage = Voltage
        self._Communication_signal_level = Communication_signal_level
        self._X2D_3D = X2D_3D
        self._PDOP = PDOP
        self._HDOP = HDOP
        self._X_axis_angle = X_axis_angle
        self._Y_axis_angle = Y_axis_angle
        self._Z_axis_angle = Z_axis_angle


    def get_device_name(self):
        # ID: 1211 - 赤麻鸭雄鸟剑湖20210123
        pattern = r":\s*(.*?)\s*-"
        result = re.search(pattern, self._Device_No)
        # print(result)
        if result == None:
            print("字段：" + self._Device_No + " 中未匹配到合法的设备名")
            return None
        return result.group(1)


    def get_time(self):
        '''
        :return:返回一个时间字符串
        时间格式：%Y-%m-%d %H:%M:%S
        '''
        time = self._Date +" " + self._Time

        datetime_obj = datetime.strptime(time, "%Y/%m/%d %H:%M:%S")
        # print(datetime_obj)
        time_str = datetime_obj.strftime(r"%Y-%m-%d %H:%M:%S")
        # print(time_str)
        return time_str

    def get_satellites(self):
        '''
        卫星数：2D（3颗）3D（大于等于4）0D（无效数据）
        :return:
        '''
        tag = self._X2D_3D
        if(tag == "3D"):
            return 3
        elif(tag == "2D"):
            return 2
        return 0

    def get_hdop(self):
        return self._HDOP

    def get_speed(self):
        # 使用正则表达式匹配出数字部分
        match = re.match(r"([\d.]+)", self._Speed)

        # 如果找到了匹配
        if match == None:
            print("速度字段没找到对应的数值")
            return None

        return match.group(1)

    def get_altitude(self):
        # 使用正则表达式匹配出带正负号的数字部分
        match = re.match(r"([-+]?\d+)", self._Altitude)

        if match == None:   # 没找到对应数值
            print("高度字段没找到对应的数值")
            return None

        return match.group(1)

    def get_longitude(self):
        '''
        :return:东经为正数，西经为负数
        '''
        if(self._Eastern_Western == "E"):
            return self._Longitude
        return -1*self._Longitude

    def get_latitude(self):
        '''
        :return:北纬为正数，南纬为负数
        '''
        if(self._North_south == "N"):
            return -1*self._Latitude
        return self._Latitude



