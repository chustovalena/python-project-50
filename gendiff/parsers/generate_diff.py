def gen_diff(data_a, data_b):
  data_a = dict(sorted(data_a.items()))
  data_b = dict(sorted(data_b.items()))
  diff = []

  for key in data_a.keys():
      if key in data_b:
          if data_a[key] == data_b[key]:
              diff.append(f"    {key}: {data_a[key]}")
          else:
              diff.append(f"  - {key}: {data_a[key]}")
              diff.append(f"  + {key}: {data_b[key]}")
      else:
          diff.append(f"  - {key}: {data_a[key]}")
  for key in data_b.keys():
      if key not in data_a:
          diff.append(f"  + {key}: {data_b[key]}")
  return '{\n' + '\n'.join(diff) + '\n}'
