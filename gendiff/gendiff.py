import os

from gendiff.config.json_parser import json_read
from gendiff.config.yaml_parser import yaml_read
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def generate_diff(filepath1, filepath2, format_name='stylish'):
    _, extension1 = os.path.splitext(filepath1)
    _, extension2 = os.path.splitext(filepath2)

    if extension1 == '.json':
        data1 = json_read(filepath1)
    elif extension1 in {'.yaml', '.yml'}:
        data1 = yaml_read(filepath1)

    if extension2 == '.json':
        data2 = json_read(filepath2)
    elif extension2 in {'.yaml', '.yml'}:
        data2 = yaml_read(filepath2)

    match format_name:
        case 'stylish':
            return stylish(build_diff(data1, data2))
        case 'plain':
            return plain(build_diff(data1, data2))


def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()).union(data2.keys()))
    result = {}

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            nested_diff = build_diff(value1, value2)
            result[key] = {
                'status': 'nested',
                'value': nested_diff
            }
        elif value1 == value2:
            result[key] = {
                'status': 'unchanged',
                'value': value1
            }
        elif key not in data1.keys():
            result[key] = {
                'status': 'added',
                'value': value2
            }
        elif key not in data2.keys():
            result[key] = {
                'status': 'removed',
                'value': value1
            }
        elif value1 != value2:
            result[key] = {
                'status': 'changed',
                'old_value': value1,
                'new_value': value2
            }

    return result
