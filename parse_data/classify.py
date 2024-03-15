import pandas

from parse_data.env import csv_headers


def get_file_class(file: str | pandas.DataFrame) -> int:
    """
    获取文件类别
    Args:
        file: 文件路径或者DataFrame
    Returns:
        文件类别, 支持env.csv_headers中的类别
    Raises:
        ValueError: 文件表头不在csv_headers中
        TypeError: 文件类型不是str或者DataFrame
    """
    if isinstance(file, str):
        if file.endswith(".csv"):
            df = pandas.read_csv(file)
        else:
            df = pandas.read_excel(file)
    elif isinstance(file, pandas.DataFrame):
        df = file
    else:
        raise TypeError("file类型错误, 请传入文件路径或者DataFrame")

    # get the header of the file
    header = set(df.columns)
    if header in csv_headers:
        location = csv_headers.index(header)
    else:
        raise ValueError("文件表头不在csv_headers中, 请检查文件表头")
    return location
