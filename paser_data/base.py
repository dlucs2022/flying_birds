from abc import ABC, abstractmethod
from pathlib import Path

import pandas

from paser_data.env import csv_headers


class ParserBase(ABC):
    def __init__(self, file: str | pandas.DataFrame, encoding: str = "GB2312"):
        """
        Args:
            file: 文件路径或者DataFrame
            encoding: 文件编码, 默认为GB2312, 对于csv文件有效
        共同属性：
            device_name：设备名
            time：时间
            satellites：卫星数
            speed：速度
            altitude：高度
            longitude：经度
            latitude：维度
        """
        if isinstance(file, str):
            assert Path(file).exists(), ValueError("文件不存在")
            if file.endswith(".csv"):
                self._df = pandas.read_csv(file, encoding=encoding)
            else:
                self._df = pandas.read_excel(file)
        elif isinstance(file, pandas.DataFrame):
            self._df = file
        else:
            raise TypeError("file类型错误, 请传入文件路径或者DataFrame")

        # 检查表头是否符合要求
        assert set(self._df.columns) in csv_headers, ValueError(
            "文件表头不在csv_headers中, 请检查文件表头"
        )

        # 用于存放处理后的数据
        self._data = {
            "device_name": None,
            "time": None,
            "satellites": None,
            "speed": None,
            "altitude": None,
            "longitude": None,
            "latitude": None,
            # "HDOP": None,
            # "VDOP": None,
        }
        self.preprocess()

    def preprocess(self):
        """
        预处理数据
        """
        self._df = self._df[self._df.notnull()]
        self._df = self._df[self._df.notna()]
        self._df = self._df.drop_duplicates()

    @abstractmethod
    def get_device_name(self):
        """
        :return:返回设备名
        """
        pass

    @abstractmethod
    def get_time(self):
        """
        :return:返回时间
        """
        pass

    @abstractmethod
    def get_satellites(self):
        """
        :return:返回卫星数
        """
        pass

    @abstractmethod
    def get_speed(self):
        """
        :return:返回速度
        """
        pass

    @abstractmethod
    def get_altitude(self):
        """
        :return:返回高度
        """
        pass

    @abstractmethod
    def get_longitude(self):
        """
        :return:返回经度
        """
        pass

    @abstractmethod
    def get_latitude(self):
        """
        :return:返回维度
        """
        pass

    # @abstractmethod
    # def get_HDOP(self):
    #     """
    #     :return:返回HDOP, 水平精度因子
    #     """
    #     pass

    # @abstractmethod
    # def get_VDOP(self):
    #     """
    #     :return:返回VDOP, 垂直精度因子
    #     """
    #     pass

    @property
    def result(self):
        if self._data["device_name"] is None:
            self.get_device_name()
        if self._data["time"] is None:
            self.get_time()
        if self._data["satellites"] is None:
            self.get_satellites()
        if self._data["speed"] is None:
            self.get_speed()
        if self._data["altitude"] is None:
            self.get_altitude()
        if self._data["longitude"] is None:
            self.get_longitude()
        if self._data["latitude"] is None:
            self.get_latitude()
        # if self._data["HDOP"] is None:
        #     self.get_HDOP()
        # if self._data["VDOP"] is None:
        #     self.get_VDOP()

        return self._data

    @property
    def dataframe(self):
        return pandas.DataFrame(self.result)

    def __getitem__(self, item: int) -> dict:
        keys = self.dataframe.iloc[item].index
        values = self.dataframe.iloc[item].values
        return dict(zip(keys, values))

    def __len__(self):
        return len(self.dataframe)
