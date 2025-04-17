from gendiff.parsers.generate_diff import gen_diff
import pytest

def test_empty_data():
	assert gen_diff({}, {}) == '{\n' + '\n}'


def test_no_second_data():
	assert gen_diff({'hey': 'karen'}, {}) == '{\n' + '  - hey: karen' + '\n}'


def test_no_first_data():
	assert gen_diff({}, {'hey': 'karen'}) == '{\n' + '  + hey: karen' + '\n}'

def same_data():
	assert gen_diff({'hello': 'world'},{'hello': 'world'}) == '{\n' + '    hey: karen' + '\n}'

def in_a_and_in_b_but_different():
	assert gen_diff({'hello': 'world'}, {'hello': 'sam'}) == '{\n' + '  - hello: world' + '\n' + '  + hello : sam' + '\n}'