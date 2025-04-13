from gendiff.parsers.generate_diff import gen_diff
import pytest

def test_empty_data():
	assert gen_diff({}, {}) == '{\n' + '\n}'


def test_no_second_data():
	assert gen_diff({'hey': 'karen'}, {}) == '{\n' + '- hey : karen' + '\n}'


def test_no_first_data():
	assert gen_diff({}, {'hey': 'karen'}) == '{\n' + '+ hey : karen' + '\n}'