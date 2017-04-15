#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cli import args
from fd import (
        files_with_same_name,
        files_with_same_size,
        files_with_same_data,
        )

technique = args['technique']
if technique == 'n':
    print("File with same name")
    for i in files_with_same_name(args['path']):
        file_name = (i[0])
        number_of_duplicate_files = len(i)
        print("{} duplicates:: {}".format(number_of_duplicate_files, file_name))

elif technique == 's':
    print("Files with same size")
    for i in files_with_same_size(args['path']):
        file_name = (i[0])
        number_of_duplicate_files = len(i)
        print("{} duplicates:: {}".format(number_of_duplicate_files, file_name))
else:
    print("Files with same data")
    for i in files_with_same_data(args['path']):
        file_name = (i[0])
        number_of_duplicate_files = len(i)
        print("{} duplicates:: {}".format(number_of_duplicate_files, file_name))
