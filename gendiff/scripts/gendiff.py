#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import parse_arguments


def main():
    arguments = parse_arguments()
    diff = generate_diff(
        arguments.first_file,
        arguments.second_file,
        arguments.format
    )
    print(diff)


if __name__ == '__main__':
    main()
