from gendiff.gendiff import generate_diff


def test_simple_json():
    with open('tests/test_data/result.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    
    assert generate_diff(
        'tests/test_data/json_files/file1.json',
        'tests/test_data/json_files/file2.json'
        ) == data


def test_simple_yaml():
    with open('tests/test_data/result.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    
    assert generate_diff(
        'tests/test_data/yaml_files/file1.yaml',
        'tests/test_data/yaml_files/file2.yaml'
        ) == data


def test_complex_json():
    with open(
        'tests/test_data/complex_result.txt', 'r', encoding='utf-8'
    ) as file:
        data = file.read()

    assert generate_diff(
        'tests/test_data/json_files/complex_file1.json',
        'tests/test_data/json_files/complex_file2.json'
    ) == data


def test_complex_yaml():
    with open(
        'tests/test_data/complex_result.txt', 'r', encoding='utf-8'
    ) as file:
        data = file.read()

    assert generate_diff(
        'tests/test_data/yaml_files/complex_file1.yaml',
        'tests/test_data/yaml_files/complex_file2.yaml'
    ) == data


def test_plain_format():
    with open(
        'tests/test_data/plain_result.txt', 'r', encoding='utf-8'
    ) as file:
        data = file.read()

    assert generate_diff(
        'tests/test_data/yaml_files/complex_file1.yaml',
        'tests/test_data/json_files/complex_file2.json',
        'plain'
    ) == data


def test_json_format():
    with open(
        'tests/test_data/json_result.txt', 'r', encoding='utf-8'
    ) as file:
        data = file.read()

    assert generate_diff(
        'tests/test_data/yaml_files/complex_file1.yaml',
        'tests/test_data/json_files/complex_file2.json',
        'json'
    ) == data
