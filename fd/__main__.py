#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cli import args
from fd import (
        files_with_same_name,
        files_with_same_size,
        files_with_same_data,
        )

technique = args['technique']
path = args['path']

if technique == 'n':
    print("File with same name")
    for files_list in files_with_same_name(path):
        print(files_list)

elif technique == 's':
    print("Files with same size")
    for files_list in files_with_same_size(path):
        print(files_list)
else:
    print("Files with same data")
    for files_list in files_with_same_data(path):
        print(files_list)
