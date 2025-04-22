def formatting(diff, depth=0):
    lines = []
    indent = ' ' * (depth * 4)
    for key, value in diff.items():
        if value['status'] == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.extend(formatting(value['children'], depth + 1))
            lines.append(f"{indent}    }}")
        elif value['status'] == 'changed':
            lines.append(f"{indent}  - {key}: {format_value(value['old_value'], depth)}")
            lines.append(f"{indent}  + {key}: {format_value(value['new_value'], depth)}")
        elif value['status'] == 'added':
            lines.append(f"{indent}  + {key}: {format_value(value['value'], depth)}")
        elif value['status'] == 'removed':
            lines.append(f"{indent}  - {key}: {format_value(value['value'], depth)}")
        elif value['status'] == 'unchanged':
            lines.append(f"{indent}    {key}: {format_value(value['value'], depth)}")
    return lines



def format_value(value, depth):
    indent = ' ' * ((depth + 1) * 4)
    bracket_indent = ' ' * (depth * 4)

    if isinstance(value, dict):
        lines = ['{']
        for key, v in value.items():
            lines.append(f"{indent}    {key}: {format_value(v, depth + 1)}")
        lines.append(f"{bracket_indent}    }}")
        return '\n'.join(lines)
    else:
        return str(value)



def res_formatting(lines):
    return "{\n" + '\n'.join(lines) + "\n}"
