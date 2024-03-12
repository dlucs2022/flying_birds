#设备名： 赤麻鸭04（雌）·KIZ122·剑湖·20220223
from paser_data.device import Device
import re
from datetime import datetime

class Machine01(Device):
    def __init__(self, X_U_FEFF_Terminal, IMEID, Time, East_West, Longitude,
                 North_South, Latitude, Speed, Heading, Altitude,
                 Temperature, Voltage, Amount_of_exercise, Satellite, HDOP,
                 VDOP, Accuracy, Effectiveness):
        '''
        对象参数和CSV文件表头对应关系
        :param X_U_FEFF_Terminal: X.U.FEFF.终端
        :param IMEID:IMEID
        :param Time:时间
        :param East_West:东西
        :param Longitude:经度
        :param North_South:南北
        :param Latitude:纬度
        :param Speed:速度
        :param Heading:航向
        :param Altitude:高度
        :param Temperature:温度
        :param Voltage:电压
        :param Amount_of_exercise:运动量
        :param Satellite:卫星
        :param HDOP:HDOP
        :param VDOP:VDOP
        :param Accuracy:精度
        :param Effectiveness:有效性
        '''

        self._X_U_FEFF_Terminal = X_U_FEFF_Terminal
        self._IMEID = IMEID
        self._Time = Time
        self._East_West = East_West
        self._Longitude = Longitude
        self._North_South = North_South
        self._Latitude = Latitude
        self._Speed = Speed
        self._Heading = Heading
        self._Altitude = Altitude
        self._Temperature = Temperature
        self._Voltage = Voltage
        self._Amount_of_exercise = Amount_of_exercise
        self._Satellite = Satellite
        self._HDOP = HDOP
        self._VDOP = VDOP
        self._Accuracy = Accuracy
        self._Effectiveness = Effectiveness

    def __str__(self):
        return f"X_U_FEFF_Terminal: {self._X_U_FEFF_Terminal}\nIMEID: {self._IMEID}\n" \
               f"Time: {self._Time}\nEast/West: {self._East_West}\n" \
               f"Longitude: {self._Longitude}\nNorth/South: {self._North_South}\n" \
               f"Latitude: {self._Latitude}\nSpeed: {self._Speed}\n" \
               f"Heading: {self._Heading}\nAltitude: {self._Altitude}\n" \
               f"Temperature: {self._Temperature}\nVoltage: {self._Voltage}\n" \
               f"Amount of Exercise: {self._Amount_of_exercise}\nSatellite: {self._Satellite}\n" \
               f"HDOP: {self._HDOP}\nVDOP: {self._VDOP}\n" \
               f"Accuracy: {self._Accuracy}\nEffectiveness: {self._Effectiveness}"

    def get_device_name(self):
        # 赤麻鸭04（雌）·KIZ122·剑湖·20220223
        pattern = r'·(.*?)·'
        result = re.search(pattern, self._X_U_FEFF_Terminal)

        if result == None:
            print("字段："+self._X_U_FEFF_Terminal+" 中未匹配到合法的设备名")
            return None
        return result.group(1)

    def get_time(self):
        '''
        :return:返回一个时间字符串
        时间格式：%Y-%m-%d %H:%M:%S
        '''
        # 2022/7/30  3:32:00
        time = self._Time

        date_format = r"%Y/%m/%d  %H:%M"
        # 将时间字符串解析为 datetime 对象
        datetime_obj = datetime.strptime(time, date_format)

        # 将 datetime 对象转换为字符串
        datetime_str = datetime_obj.strftime(r"%Y-%m-%d %H:%M:%S")

        return datetime_str

    def get_satellites(self):
        if (self._Satellite >= 4):
            return 3
        elif (self._Satellite == 3):
            return 2
        return 0

    def get_hdop(self):
        return self._HDOP

    def get_speed(self):
        return self._Speed

    def get_altitude(self):
        return self._Altitude

    def get_longitude(self):
        '''
        :return:东经为正数，西经为负数
        '''
        if self._East_West == "西经":
            return -1*self._Longitude
        return self._Longitude

    def get_latitude(self):
        '''
        :return:北纬为正数，南纬为负数
        '''
        if self._North_South == "南维":
            return -1*self._Latitude
        return self._Latitude



