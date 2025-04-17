import json
import yaml
from pathlib import Path

def open_files(file1_path, file2_path):
	file_path = Path(file1_path)
	if file_path.suffix.lower() == '.json':
		with open(file1_path, 'r') as file:
			data_a = json.load(file)
		with open(file2_path, 'r') as file:
			data_b = json.load(file)
	elif file_path.suffix.lower() in ['.yaml', '.yml']:
		with open(file1_path, 'r') as file:
			data_a = yaml.safe_load(file)
		with open(file2_path, 'r') as file:
			data_b = yaml.safe_load(file)
	return data_a, data_b