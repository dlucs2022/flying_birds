from datetime import datetime

import pandas

from paser_data.base import ParserBase
from paser_data.tools import get_satellite_dim


class Parser02(ParserBase):
    def __init__(self, file: str | pandas.DataFrame, encoding: str = "GB2312"):
        super().__init__(file, encoding=encoding)

    def get_device_name(self) -> pandas.Series:
        device_series = self._df["UUID"].astype(dtype="string", copy=True)
        self._data["device_name"] = device_series
        return device_series

    def get_time(self) -> pandas.Series:
        """
        时间格式：%Y-%m-%d %H:%M:%S
        """
        time_series = (
            self._df["Collecting.time"]
            .astype(dtype="string", copy=True)
            .apply(
                lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )
        )
        self._data["time"] = time_series
        return time_series

    def get_satellites(self) -> pandas.Series:
        """
        获取定位纬度，卫星上大于等于4为3D，3为2D，小于3为0D
        """
        satellites_series = (
            self._df["Satellite.used"]
            .astype("Int8", copy=True)
            .apply(get_satellite_dim)
        )
        self._data["satellites"] = satellites_series
        return satellites_series

    # def get_HDOP(self) -> pandas.Series:
    #     """
    #     获取水平精度因子
    #     """
    #     hdop_series = self._df["HDOP"].astype(dtype="Float32", copy=True)
    #     self._data["HDOP"] = hdop_series
    #     return hdop_series

    # def get_VDOP(self) -> pandas.Series:
    #     """
    #     获取垂直精度因子, 单位米
    #     """
    #     vdop_series = self._df["VDOP"].astype(dtype="Float32", copy=True)
    #     self._data["VDOP"] = vdop_series
    #     return vdop_series

    def get_speed(self) -> pandas.Series:
        """
        单位km/h
        """
        speed_series = self._df["Speed"].astype(dtype="Float32", copy=True)
        self._data["speed"] = speed_series
        return speed_series

    def get_altitude(self) -> pandas.Series:
        """
        单位米
        """
        altitude_series = self._df["Altitude"].astype(dtype="Float32", copy=True)
        self._data["altitude"] = altitude_series
        return altitude_series

    def get_longitude(self) -> pandas.Series:
        """
        东经为正数，西经为负数
        """
        longitude_series = self._df["Longitude"].astype(dtype="Float32", copy=True)
        self._data["longitude"] = longitude_series
        return longitude_series

    def get_latitude(self) -> pandas.Series:
        """
        北纬为正数，南纬为负数
        """
        latitude_series = self._df["Latitude"].astype(dtype="Float32", copy=True)
        self._data["latitude"] = latitude_series
        return latitude_series
