#赤麻鸭9978 efeb37b5945d
from trans.device import Device
from datetime import datetime

class Machine02(Device):
    def __init__(self,UUID,Transmitting_time,Collecting_time,Longitude,Latitude,
                 Altitude,Altitude_Ellipsoid,Speed,NED_Speed,Course,
                 Satellite_used,Positioning_mode,HorAccuracy,VerAccuracy,GPS_time_consumption,
                 Data_Source,HDOP,VDOP):

        self._UUID = UUID
        self._Transmitting_time = Transmitting_time
        self._Collecting_time = Collecting_time
        self._Longitude = Longitude
        self._Latitude = Latitude
        self._Altitude = Altitude
        self._Altitude_Ellipsoid = Altitude_Ellipsoid
        self._Speed = Speed
        self._NED_Speed = NED_Speed
        self._Course = Course
        self._Satellite_used = Satellite_used
        self._Positioning_mode = Positioning_mode
        self._HorAccuracy = HorAccuracy
        self._VerAccuracy = VerAccuracy
        self._GPS_time_consumption = GPS_time_consumption
        self._Data_Source = Data_Source
        self._HDOP = HDOP
        self._VDOP = VDOP

    def __str__(self):
        return f"UUID: {self._UUID}\nTransmitting Time: {self._Transmitting_time}\n" \
               f"Collecting Time: {self._Collecting_time}\nLongitude: {self._Longitude}\n" \
               f"Latitude: {self._Latitude}\nAltitude: {self._Altitude}\n" \
               f"Altitude Ellipsoid: {self._Altitude_Ellipsoid}\nSpeed: {self._Speed}\n" \
               f"NED Speed: {self._NED_Speed}\nCourse: {self._Course}\n" \
               f"Satellite Used: {self._Satellite_used}\nPositioning Mode: {self._Positioning_mode}\n" \
               f"Horizontal Accuracy: {self._HorAccuracy}\nVertical Accuracy: {self._VerAccuracy}\n" \
               f"GPS Time Consumption: {self._GPS_time_consumption}\nData Source: {self._Data_Source}\n" \
               f"HDOP: {self._HDOP}\nVDOP: {self._VDOP}"

    def get_device_name(self):
        return self._UUID

    def get_time(self):
        '''
        :return:返回一个时间字符串
        时间格式：%Y-%m-%d %H:%M:%S
        '''
        # 2022 - 03 - 09T08: 56:04Z
        time = self._Collecting_time
        datetime_obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
        # print(datetime_obj)
        time_str = datetime_obj.strftime(r"%Y-%m-%d %H:%M:%S")
        return time_str

    def get_satellites(self):
        if(self._Satellite_used >= 4):
            return 3
        elif(self._Satellite_used == 3):
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
        return self._Longitude

    def get_latitude(self):
        '''
        :return:北纬为正数，南纬为负数
        '''
        return self._Altitude
