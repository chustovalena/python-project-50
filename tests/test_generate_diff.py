from gendiff.parsers.generate_diff import generate_diff
import pytest

def test_empty_data():
	assert generate_diff({}, {}) == '{\n' + '\n}'


def test_no_second_data():
	assert generate_diff({'hey': 'karen'}, {}) == '{\n' + '  - hey: karen' + '\n}'


def test_no_first_data():
	assert generate_diff({}, {'hey': 'karen'}) == '{\n' + '  + hey: karen' + '\n}'

def test_same_data():
	assert generate_diff({'hello': 'world'},{'hello': 'world'}) == '{\n' + '    hello: world' + '\n}'

def test_in_a_and_in_b_but_different():
	assert generate_diff({'hello': 'world'}, {'hello': 'sam'}) == '{\n' + '  - hello: world' + '\n' + '  + hello: sam' + '\n}'