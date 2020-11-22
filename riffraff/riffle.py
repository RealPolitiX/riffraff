#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def riffle(*arr):
    """
    Interleave multiple arrays of the same number of elements.

    **Parameter**\n
    *arr: array
        A number of arrays

    **Return**\n
    riffarr: 1D array
        An array with interleaving elements from each input array.
    """

    arr = (map(np.ravel, arr))
    arrlen = np.array(map(len, arr))

    try:
        riffarr = np.vstack(arr).reshape((-1,), order='F')
        return riffarr
    except:
        raise ValueError('Input arrays need to have the same number of elements!')