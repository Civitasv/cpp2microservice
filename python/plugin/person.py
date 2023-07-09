import ctypes

from . import lib


def create_person(name, age):
    lib.create_person.restype = ctypes.c_void_p
    lib.create_person.argtypes = [ctypes.c_char_p, ctypes.c_int]

    return lib.create_person(name.encode("utf-8"), age)


def print_person(person):
    lib.get_person_name.restype = ctypes.c_char_p
    lib.get_person_name.argtypes = [ctypes.c_void_p]

    lib.get_person_age.restype = ctypes.c_int
    lib.get_person_age.argtypes = [ctypes.c_void_p]

    name = lib.get_person_name(person).decode("utf-8")
    age = lib.get_person_age(person)

    return f"name: {name}, age: {age}"


def delete_person(person):
    lib.delete_person.argtypes = [ctypes.c_void_p]
    lib.delete_person(person)
