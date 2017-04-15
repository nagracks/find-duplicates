#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


parser = argparse.ArgumentParser(
                description='Find Duplicates'
                )
parser.add_argument(
        '-p', '--path',
        dest='path',
        action='store',
        required=True,
        help="""
        Full path
        """
        )
parser.add_argument(
        '-t', '--technique',
        dest='technique',
        action='store',
        default='d',
        help="""
        Values can be files with same [n]ame, files with same [s]ize or
        files with same [d]ata
        """
        )

args = vars(parser.parse_args())

