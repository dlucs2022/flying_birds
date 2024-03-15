# 解析原始数据
import pandas
from parse_data.base import ParserBase
from parse_data.device_01_parser import Parser01
from parse_data.device_02_parser import Parser02
from parse_data.device_03_parser import Parser03
from parse_data.env import csv_headers


class OriginParser:
    def __init__(self, file: str | pandas.DataFrame, encoding: str = "gb2312"):
        if isinstance(file, pandas.DataFrame):
            self._df = file
        else:
            if file.endswith(".csv"):
                self._df = pandas.read_csv(file, encoding=encoding)
            else:
                self._df = pandas.read_excel(file)

        assert set(self._df.columns) in csv_headers, ValueError(
            "文件表头不在csv_headers中, 请检查文件表头"
        )

        self.preprocess()

    def preprocess(self):
        self._df = self._df[self._df.notnull()]
        self._df = self._df[self._df.notna()]
        self._df = self._df.drop_duplicates()

    @property
    def type(self):
        return csv_headers.index(set(self._df.columns))

    def __getitem__(self, item: int) -> dict:
        keys = self._df.iloc[item].index
        values = self._df.iloc[item].values
        return dict(zip(keys, values))


def parse_data(file: str | pandas.DataFrame, encoding: str = "gb2312") -> OriginParser:
    """
    解析原始数据
    :param file: 数据文件，支持xls，xlsx，csv格式文件或是DataFrame
    :param encoding: 文件编码，用于解码csv文件
    :return: 解析原始数据的对象
    """
    return OriginParser(file, encoding)


def parse_common_data(
    file: str | pandas.DataFrame, encoding: str = "gb2312"
) -> ParserBase:
    if isinstance(file, pandas.DataFrame):
        df = file
    else:
        if file.endswith(".csv"):
            df = pandas.read_csv(file, encoding=encoding)
        else:
            df = pandas.read_excel(file)
    index = csv_headers.index(set(df.columns))

    match index:
        case 0:
            Parser = Parser01
        case 1:
            Parser = Parser02
        case 2:
            Parser = Parser03
        case _:
            raise ValueError("文件表头不匹配")

    return Parser(file, encoding)
