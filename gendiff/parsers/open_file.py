import json


def open_files(file1_path, file2_path):
	with open(file1_path, 'r') as file:
		data_a = json.load(file)
	with open(file2_path, 'r') as file:
		data_b = json.load(file)

	return data_a, data_b