#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


def main():
    pars_params = {
        'prog': 'gendiff',
        'usage': 'gendiff [-h] [-f FORMAT] first_file second_file',
        'description': 'Compares two configuration '
                       'files and shows a difference.',
        'epilog': 'The utility supports .json, .yml and yaml file extensions.'
    }

    parser = argparse.ArgumentParser(**pars_params)
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format",
                        help="set format of output",
                        default='stylish', required=False,
                        choices=['stylish', 'plain'])
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
