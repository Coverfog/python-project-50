import json


def json_format(data):

    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    return json_str
