import os


def is_csv(file:str):
    filename, file_extension = os.path.splitext(file)
    if file_extension.lower() != '.csv':
        return 0
    return 1




