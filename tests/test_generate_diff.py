from gendiff.parsers.generate_diff import gen_diff


def empty_data():
	assert gen_diff({}, {}) == '{\n' + '\n}'


def no_second_data():
	assert gen_diff({'hey': 'karen'}, {}) == '{\n' + '- hey : karen' + '\n}'


def no_first_data():
	assert gen_diff({}, {'hey': 'karen'}) == '{\n' + '+ hey : karen' + '\n}'