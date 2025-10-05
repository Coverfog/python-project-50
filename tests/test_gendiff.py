from gendiff.gendiff import generate_diff


def test_plain_json():
    with open('tests/test_data/result.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    
    assert generate_diff(
        'tests/test_data/json_files/file1.json',
        'tests/test_data/json_files/file2.json'
        ) == data


def test_plain_yaml():
    with open('tests/test_data/result.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    
    assert generate_diff(
        'tests/test_data/yaml_files/file1.yaml',
        'tests/test_data/yaml_files/file2.yaml'
        ) == data
