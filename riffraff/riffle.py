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
    minlen = np.min(arrlen)
    if not(np.prod(arrlen == minlen)):
        arr = [a[:minlen] for a in arr]
    
    riffarr = np.vstack(arr).reshape((-1,), order='F')

    return riffarr