def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return str(value)


def format_plain(diff, path=''):
    lines = []
    for key, node in sorted(diff.items()):
        property_path = f"{path}.{key}" if path else key
        status = node['status']
        if status == 'added':
            value = stringify(node['value'])
            lines.append(f"Property '{property_path}' was added with value: {value}")
        elif status == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif status == 'changed':
            old = stringify(node['old_value'])
            new = stringify(node['new_value'])
            lines.append(f"Property '{property_path}' was updated. From {old} to {new}")
        elif status == 'nested':
            nested_result = format_plain(node['children'], property_path)
            if nested_result:
                lines.extend(nested_result)
    return lines



def res_formatting(lines):
    return '\n'.join(lines)