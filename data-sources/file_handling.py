import datetime
from pathlib import Path


def get_file_name(file_type, symbol):
    root = Path.home() / "_work/_tempdata"  # todo: get root from config
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    json_file = f"{file_type}-{symbol}-{timestamp}.json"
    file_name_and_path = Path(root) / symbol / json_file
    file_name_and_path.parent.mkdir(parents=True, exist_ok=True)
    return file_name_and_path
