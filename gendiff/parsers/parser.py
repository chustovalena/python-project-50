import argparse


def parser_args():
	parser = argparse.ArgumentParser(
		description='Compares two configuration files and shows a difference.')
	
	parser.add_argument('first_file')
	parser.add_argument('second_file')
	parser.add_argument(
        '-f', '--format',
        choices=['stylish', 'plain'],
        default='stylish',
        help='set format of output (stylish, plain)'
    )
	args = parser.parse_args()

	return args
