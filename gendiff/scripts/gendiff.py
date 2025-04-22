from gendiff.parsers.generate_diff import generate_diff
from gendiff.parsers.parser import parser_args


def main():
    args = parser_args()

    format_name = args.format or 'stylish'

    diff = generate_diff(args.first_file, args.second_file, format_name)

    print(diff)


if __name__ == '__main__':
    main()
