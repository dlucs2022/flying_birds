import pandas

from paser_data.env import csv_headers


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
