#!/usr/bin/env python3

import argparse

from gendiff import generate_diff
from gendiff.formaters.formater_plain import plain
from gendiff.formaters.formater_stylish import stylish


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default=stylish, help='set format of output'
    )
    args = parser.parse_args()

    if args.format == 'plain':
        diff = generate_diff(args.first_file, args.second_file, format=plain)
    else:
        diff = generate_diff(args.first_file, args.second_file, format=stylish)

    print(diff)


if __name__ == '__main__':
    main()
