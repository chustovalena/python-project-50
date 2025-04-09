from gendiff.parsers.parser import parser_args
from gendiff.parsers.open_file import open_files
from gendiff.parsers.generate_diff import gen_diff

def main():
    args = parser_args()

    data_a, data_b = open_files(args.first_file, args.second_file)

    diff = gen_diff(data_a, data_b)

    print(diff)



if __name__ == '__main__':
    main()
