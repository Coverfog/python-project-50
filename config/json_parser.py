import json


def json_read(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
