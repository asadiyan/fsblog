import os
import pathlib
import datetime


def create_directory(path: str):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)


def create_file(file_path: str, data: str):
    with open(file_path, 'w') as fi:
        fi.write(data)


def get_date_time(path_to_file):
    return datetime.datetime.fromtimestamp(os.path.getctime(path_to_file))


def date_to_str(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d")
