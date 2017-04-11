#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import collections
import hashlib


def dir_walker(path, ignore_ext=[], ignore_dirs=[]):
    """Walks recursively from give path

    Parameters
    ----------
    path : str
        Root path from where you want to start recursive walking
    ignore_ext : list, optional
        Extension that you wan to ignore. If `ignore_ext=['.pyc']` is
        provided then it will not yield `*.pyc` files.
    ignore_dirs: list, optional
        List of directories whose files you don't want

    Yields
    ------
    str
        File's full path
    """
    for root, dirs, files in os.walk(path):
        dirs[:] = (
                dir_ for dir_ in dirs
                if dir_ not in ignore_dirs
                )
        files = (
                file_ for file_ in files
                if os.path.splitext(file_)[-1] not in ignore_ext
                )
        for file_name in files:
            yield os.path.join(root, file_name)


def md5_hash(filepath):
    m = hashlib.md5()
    try:
        with open(filepath, 'rb') as f_in:
            while True:
                data = f_in.read(1024)
                if not data:
                    break
                m.update(data)
    except (FileNotFoundError, OSError) as e:
        print(e)
    return m.hexdigest()


def files_with_same_name(path):
    """Provide list of files with same name

    Parameters
    ----------
    path : str
        Full path to directory

    Returns
    -------
    list
        Full path of Files with same name
    """
    all_files = list(dir_walker(path))

    counter = collections.Counter()
    for file_name in all_files:
        base_name = file_name.split('/')[-1]
        counter[base_name] += 1
    duplicate_names = [k for k, v in counter.items() if v > 1]

    dup_files = []
    for file_path in all_files:
        base_name = file_path.split('/')[-1]
        if base_name in duplicate_names:
            dup_files.append(file_path)
    return dup_files
