import pandas

from parse_data.base import ParserBase
from datetime import datetime


class Parser03(ParserBase):
    def __init__(self, file: str | pandas.DataFrame, encoding: str = "GB2312"):
        super().__init__(file, encoding=encoding)
        self.preprocess()

    def preprocess(self):
        """
        预处理数据
        """
        self._df: pandas.DataFrame = self._df[~self._df["X2D.3D"].str.contains("/")]
        self._df: pandas.DataFrame = self._df[~self._df["高度"].str.contains("/")]
        super().preprocess()

    def get_device_name(self):
        pat = r".*?:(?P<device>\d+)-.+"
        device_series = (
            self._df["设备号"]
            .astype(dtype="string", copy=True)
            .str.replace(pat, lambda x: x.group("device"), regex=True)
        )
        self._data["device_name"] = device_series
        return device_series

    def get_time(self):
        """
        时间格式：%Y-%m-%d %H:%M:%S
        """
        date_series = self._df["日期"].astype(dtype="string", copy=True)
        time_series = self._df["时间"].astype(dtype="string", copy=True)
        time_series = date_series + " " + time_series
        time_series = time_series.apply(
            lambda x: datetime.strptime(x, "%Y/%m/%d %H:%M:%S").strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
        self._data["time"] = time_series
        return time_series

    def get_satellites(self):
        """
        获取卫星维度
        """
        satellites_series = (
            self._df["X2D.3D"]
            .astype("string", copy=True)
            .str.replace(
                r".*?(?P<satellite>\d+).+",
                lambda x: x.group("satellite"),
                regex=True,
            )
            .astype("int8")
        )
        self._data["satellites"] = satellites_series
        return satellites_series

    # def get_HDOP(self):
    #     hdop_series = self._df["HDOP"].astype(dtype="Float32", copy=True)
    #     self._data["HDOP"] = hdop_series
    #     return hdop_series

    def get_speed(self):
        pat = r".*?(?P<speed>\d+(?:\.\d+)?).+"
        speed_series = (
            self._df["速度"]
            .astype(dtype="string", copy=True)
            .str.replace(pat, lambda x: x.group("speed"), regex=True)
            .astype("Float32")
        )
        self._data["speed"] = speed_series
        return speed_series

    def get_altitude(self):
        def repl(x):
            if x.group("sign") == "+":
                return x.group("altitude")
            return "-" + x.group("altitude")

        altitude_series = (
            self._df["高度"]
            .astype(dtype="string", copy=True)
            .str.replace(
                r".*?(?P<sign>[-+])(?P<altitude>\d+(?:\.\d+)?).+",
                repl,
                regex=True,
            )
        )
        altitude_series.astype("Float32")
        self._data["altitude"] = altitude_series
        return altitude_series

    def get_longitude(self):
        """
        东经为正数，西经为负数
        """
        longitude = self._df["经度"].astype(dtype="Float32", copy=True)
        sign = (
            self._df["东西经"]
            .astype(dtype="string")
            .str.replace(
                r"(.+)",
                lambda x: "1" if "E" in x.group(1) else "-1",
                regex=True,
            )
            .astype("Int8")
        )
        longitude_series = longitude * sign
        self._data["longitude"] = longitude_series
        return longitude_series

    def get_latitude(self):
        """
        北纬为正数，南纬为负数
        """
        latitude = self._df["纬度"].astype(dtype="Float32", copy=True)
        sign = (
            self._df["南北纬"]
            .astype(dtype="string", copy=True)
            .str.replace(
                r"(.+)",
                lambda x: "1" if "N" in x.group(1) else "-1",
                regex=True,
            )
            .astype("Int8")
        )
        latitude_series = latitude * sign
        self._data["latitude"] = latitude_series
        return latitude_series
