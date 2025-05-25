import json

import pytest

from gendiff.formatters.format import formatting
from gendiff.formatters.format import res_formatting as res_format
from gendiff.formatters.format_json import format_json
from gendiff.formatters.format_plain import format_plain, res_formatting
from gendiff.parsers.generate_diff import gen_diff, generate_diff


@pytest.mark.parametrize(
	"data_a, data_b, expected",
	[
        ({}, {}, '{\n\n}'),
        ({'hey': 'karen'}, {}, '{\n  - hey: karen\n}'),
        ({}, {'hey': 'karen'}, '{\n  + hey: karen\n}'),
        ({'hello': 'world'}, {'hello': 'world'}, '{\n    hello: world\n}'),
        (
            {'hello': 'world'}, {'hello': 'sam'},
            '{\n  - hello: world\n  + hello: sam\n}'
            ),
    ]
)
def test_gen_diff_stylish(data_a, data_b, expected):
	diff = gen_diff(data_a, data_b)
	lines = formatting(diff)
	assert res_format(lines) == expected


@pytest.mark.parametrize(
    "data_a, data_b, expected",
    [
        (
            {'hello': 'world'}, {'hello': 'sam'},
            "Property 'hello' was updated. From 'world' to 'sam'"),
        (
            {'a': 1}, {'a': 1, 'b': True},
            "Property 'b' was added with value: true"),
        (
            {'a': 1, 'b': 2}, {'b': 2},
            "Property 'a' was removed"),
    ]
)
def test_gen_diff_plain(data_a, data_b, expected):
    diff = gen_diff(data_a, data_b)
    lines = format_plain(diff)
    assert res_formatting(lines) == expected


@pytest.mark.parametrize(
    "data_a, data_b",
    [
        ({'key': 'value'}, {'key': 'value'}),
        ({'key': 'value'}, {'key': 'new_value'}),
        ({}, {'key': 'value'}),
    ]
)
def test_gen_diff_json(data_a, data_b):
    diff = gen_diff(data_a, data_b)
    result = format_json(diff)
    parsed = json.loads(result)
    assert isinstance(parsed, dict)
    assert set(parsed.keys()) == set(diff.keys())


def test_generate_diff(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    data1 = {"key": "value"}
    data2 = {"key": "value", "another": 123}

    file1.write_text(json.dumps(data1))
    file2.write_text(json.dumps(data2))
    result = generate_diff(file1, file2, format_name='plain')
    assert result == "Property 'another' was added with value: 123"
    result = generate_diff(file1, file2)
    assert result == '{\n  + another: 123\n    key: value\n}'
    diff = gen_diff(data1, data2)
    assert generate_diff(file1, file2, 'json') == json.dumps(diff, indent=4)

