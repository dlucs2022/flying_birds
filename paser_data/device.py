from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, device_name, time, satellites,hdop,speed,altitude, longitude, latitude):
        """
        初始化Device对象

        参数:
        device_name：设备名
        time：时间
        satellites：卫星数
        speed：速度
        altitude：高度
        longitude：经度
        latitude：维度
        """
        self._device_name = device_name
        self._time = time
        self._satellites = satellites
        self._hdop = hdop
        self._speed = speed
        self._altitude = altitude
        self._longitude = longitude
        self._latitude = latitude

    @abstractmethod
    def get_device_name(self):
        pass

    @abstractmethod
    def get_time(self):
        '''
        :return:输出为一个时间字符串，统一格式为：%Y-%m-%d %H:%M:%S
        例如：2022-03-09 08:56:04
        '''
        pass

    @abstractmethod
    def get_satellites(self):
        '''
        卫星数：返回一个数字，其含义如下
        0：表示卫星数小于3颗
        2：表示卫星数等于3颗
        3表示卫星数大于等于4颗
        :return:
        '''
        pass

    @abstractmethod
    def get_hdop(self):
        pass

    @abstractmethod
    def get_speed(self):
        '''
        返回一个数字，单位km/h
        :return:
        '''
        pass

    @abstractmethod
    def get_altitude(self):
        '''
        返回数字，单位m
        :return:
        '''
        pass

    @abstractmethod
    def get_longitude(self):
        '''
        :return:东经为正数，西经为负数
        '''
        pass

    @abstractmethod
    def get_latitude(self):
        '''
        :return:北纬为正数，南纬为负数
        '''
        pass

    def get_public_properties(self):
        '''
        当前三张csv表共同的字段有如下几个：
            设备名，时间，卫星数，HDOP，速度，高度，经度，维度
        :return:返回所有公共属性所构成的一个字典
        '''
        propertise_dict = {
            "device_name": self.get_device_name(),
            "time": self.get_time(),
            "satellites": self.get_satellites(),
            "speed": self.get_speed(),
            "altitude": self.get_altitude(),
            "longitude": self.get_longitude(),
            "latitude": self.get_latitude()
        }
        return propertise_dict