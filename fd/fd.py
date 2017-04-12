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
        # Filter dirs and files with respect to ignore_ext and
        # ignore_dirs
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
    """Get md5 hash of a file

    Parameters
    ----------
    filepath : str
        Path of file

    Returns
    -------
    str
        md5 hash, hexadecimal number
    """
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
    record = collections.defaultdict(list)

    for file_path in dir_walker(path):
        base_name = file_path.split('/')[-1]
        record[base_name].append(file_path)

    for base_name in record.keys():
        paths = record[base_name]
        if len(paths) > 1:
            for path in paths:
                yield path

