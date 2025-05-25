import json

import yaml

from gendiff.parsers.open_file import open_files


def test_open_json_files(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    data1 = {"key": "value"}
    data2 = {"another": 123}

    file1.write_text(json.dumps(data1))
    file2.write_text(json.dumps(data2))

    result1, result2 = open_files(file1, file2)
    assert result1 == data1
    assert result2 == data2


def test_open_yaml_files(tmp_path):
    file1 = tmp_path / "file1.yaml"
    file2 = tmp_path / "file2.yaml"
    data1 = {"foo": "bar"}
    data2 = {"baz": True}

    file1.write_text(yaml.dump(data1))
    file2.write_text(yaml.dump(data2))

    result1, result2 = open_files(file1, file2)
    assert result1 == data1
    assert result2 == data2


def test_open_mixed_files(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.yaml"
    data1 = {"json": "data"}
    data2 = {"yaml": "data"}

    file1.write_text(json.dumps(data1))
    file2.write_text(yaml.dump(data2))

    result1, result2 = open_files(file1, file2)
    assert result1 == data1
    assert result2 == data2