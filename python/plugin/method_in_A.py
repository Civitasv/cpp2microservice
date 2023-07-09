import ctypes

from . import lib


def static_method():
    static_method = lib.c_call_method_in_A
    static_method.restype = ctypes.c_int
    static_method.argtypes = []

    return static_method()
