from gendiff.formatters.format import formatting
from gendiff.formatters.format import res_formatting as res_format
from gendiff.formatters.format_json import format_json
from gendiff.formatters.format_plain import format_plain, res_formatting


def gen_diff(data_a, data_b):
    unchanged = {
    key for key in data_a.keys() & data_b.keys() if data_a[key] == data_b[key]
    }
    common = data_a.keys() & data_b.keys() - unchanged
    added = data_b.keys() - data_a.keys()
    removed = data_a.keys() - data_b.keys()

    diff = {}

    for key in sorted(data_a.keys() | data_b.keys()):
        if key in unchanged:
            diff[key] = {'status': 'unchanged', 'value': data_a[key]}
        elif key in common:
            if isinstance(data_a[key], dict) and isinstance(data_b[key], dict):
                diff[key] = {
                'status': 'nested',
                'children': gen_diff(data_a[key], data_b[key])
                }
            else:
                diff[key] = {
                'status': 'changed',
                'old_value': data_a[key],
                'new_value': data_b[key]
                }
        elif key in added:
            diff[key] = {'status': 'added', 'value': data_b[key]}
        elif key in removed:
            diff[key] = {'status': 'removed', 'value': data_a[key]}

    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    from gendiff.parsers.open_file import open_files

    data_a, data_b = open_files(file_path1, file_path2)
    diff = gen_diff(data_a, data_b)

    if format_name == 'stylish':
        lines = formatting(diff)
        return res_format(lines)
    elif format_name == 'plain':
        lines = format_plain(diff)
        return res_formatting(lines)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")
