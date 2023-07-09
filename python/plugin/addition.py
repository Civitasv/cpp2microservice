import ctypes

from . import lib


def add(a, b):
    add_func = lib.c_add
    add_func.restype = ctypes.c_int
    add_func.argtypes = [ctypes.c_int, ctypes.c_int]

    return add_func(a, b)
