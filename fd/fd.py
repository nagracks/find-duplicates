#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
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
