#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cli import args
from fd import (
        files_with_same_name,
        files_with_same_size,
        files_with_same_data,
        duplicates_summary,
        )

technique = args['technique']
if technique == 'n':
    print("File with same name")
    for i in files_with_same_name(args['path']):
        duplicates_summary(i)

elif technique == 's':
    print("Files with same size")
    for i in files_with_same_size(args['path']):
        duplicates_summary(i)
else:
    print("Files with same data")
    for i in files_with_same_data(args['path']):
        duplicates_summary(i)
