import json


with open ('parsers/file1.json', 'r') as file:
	data_a = json.load(file)
with open ('parsers/file2.json', 'r') as file:
	data_b = json.load(file)