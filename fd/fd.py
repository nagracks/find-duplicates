#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import hashlib
import os


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
        dirs[:] = (d for d in dirs if d not in ignore_dirs)
        files = (
                f for f in files
                if os.path.splitext(f)[-1] not in ignore_ext
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
    except (OSError, IOError) as e:
        pass
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
            yield paths


def files_with_same_data(path):
    """Provide list of files with same data

    Parameters
    ----------
    path : str
        Full path to directory

    Returns
    -------
    list
        Full path of Files with same data
    """
    record = collections.defaultdict(list)

    for file_path in dir_walker(path):
        hash_value = md5_hash(file_path)
        record[hash_value].append(file_path)

    for hash_value in record.keys():
        paths = record[hash_value]
        if len(paths) > 1:
            yield paths


def files_with_same_size(path):
    """Provide list of files with same size

    Parameters
    ----------
    path : str
        Full path to directory

    Returns
    -------
    list
        Full path of Files with same size
    """
    record = collections.defaultdict(list)

    try:
        for file_path in dir_walker(path):
            size = os.path.getsize(file_path)
            record[size].append(file_path)

        for size in record.keys():
            paths = record[size]
            if len(paths) > 1:
                yield paths
    except Exception as e:
        raise(e)


def duplicates_summary(duplicate_files_list):
    file_name = duplicate_files_list[0]
    number_of_duplicate_files = len(file_name)
    print("{} duplicates:: {}".format(number_of_duplicate_files, file_name))
