#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


# Dirs
root_dir =  '/tmp/fd_test_dir'
nested_dir = os.path.join(root_dir, 'nested_dir')

# Make dirs
os.makedirs(root_dir, exist_ok=True)
os.makedirs(nested_dir, exist_ok=True)

# Files lists
file_names = [
        'test1', 'test2'
        ]
file_names_for_nested_dir = [
        'test1', 'test2', 'test3'
        ]

# Create files
for file_name in file_names:
    file_path = os.path.join(root_dir, file_name)
    with open(file_path, 'a') as f_out:
        pass
for file_name in file_names_for_nested_dir:
    file_path = os.path.join(nested_dir, file_name)
    with open(file_path, 'a') as f_out:
        pass
