from datetime import datetime

import pandas

from paser_data.base import ParserBase
from paser_data.tools import get_satellite_dim


class Parser01(ParserBase):
    def __init__(self, file: str | pandas.DataFrame, encoding: str = "gb2312"):
        super().__init__(file, encoding=encoding)

    def get_device_name(self) -> pandas.Series:
        # 赤麻鸭04（雌）·KIZ122·剑湖·20220223
        device_series = self._df["X.U.FEFF.终端"]
        pat = r".*?·(?P<device>\w+)·.+"
        device_series = device_series.astype(dtype="string", copy=True).str.replace(
            pat, lambda x: x.group("device"), regex=True
        )
        self._data["device_name"] = device_series
        return device_series

    def get_time(self) -> pandas.Series:
        """
        时间格式：%Y-%m-%d %H:%M:%S
        """
        time_series = self._df["时间"]
        time_series = time_series.astype(dtype="string", copy=True).apply(
            lambda x: datetime.strptime(x, "%Y/%m/%d %H:%M").strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
        self._data["time"] = time_series
        return time_series

    def get_satellites(self) -> pandas.Series:
        """
        获取定位纬度，卫星上大于等于4为3D，3为2D，小于3为0D
        """

        satellites_series = self._df["卫星"]
        satellites_series = satellites_series.astype("Int8", copy=True).apply(
            get_satellite_dim
        )
        self._data["satellites"] = satellites_series
        return satellites_series

    # def get_HDOP(self) -> pandas.Series:
    #     """
    #     获取水平精度因子
    #     """
    #     hdop_series = self._df["HDOP"]
    #     hdop_series = hdop_series.astype(dtype="Float32", copy=True)
    #     self._data["HDOP"] = hdop_series
    #     return hdop_series

    # def get_VDOP(self) -> pandas.Series:
    #     """
    #     获取垂直精度因子, 单位米
    #     """
    #     vdop_series = self._df["VDOP"]
    #     vdop_series = vdop_series.astype(dtype="Float32", copy=True)
    #     self._data["VDOP"] = vdop_series
    #     return vdop_series

    def get_speed(self) -> pandas.Series:
        """
        单位km/h
        """
        speed_series = self._df["速度"]
        speed_series = speed_series.astype(dtype="Float32", copy=True)
        self._data["speed"] = speed_series
        return speed_series

    def get_altitude(self) -> pandas.Series:
        """
        单位米
        """
        altitude_series = self._df["高度"]
        altitude_series = altitude_series.astype(dtype="Float32", copy=True)
        self._data["altitude"] = altitude_series
        return altitude_series

    def get_latitude(self) -> pandas.Series:
        """
        北纬为正数，南纬为负数
        """
        latitude = self._df["纬度"].astype(dtype="Float32", copy=True)
        sign = self._df["南北"] = (
            self._df["南北"]
            .astype(dtype="string")
            .str.replace(
                r"(.+)",
                lambda x: "1" if "北纬" in x.group(1) else "-1",
                regex=True,
            )
            .astype("Int8")
        )
        latitude_series = latitude * sign
        self._data["latitude"] = latitude_series
        return latitude_series

    def get_longitude(self) -> pandas.Series:
        """
        东经为正数，西经为负数
        """
        longitude = self._df["经度"].astype(dtype="Float32", copy=True)
        sign = (
            self._df["东西"]
            .astype(dtype="string", copy=True)
            .str.replace(
                r"(.+)",
                lambda x: "1" if "东经" in x.group(1) else "-1",
                regex=True,
            )
            .astype("Int8")
        )

        longitude_series = longitude * sign
        self._data["longitude"] = longitude_series
        return longitude_series
