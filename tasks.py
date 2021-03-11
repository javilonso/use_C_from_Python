import cffi
import invoke
import pathlib
import sys
import os
import shutil
import re
import glob

on_win = sys.platform.startswith("win")

@invoke.task
def clean(c):
    """ Remove any built objects """
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib",
        "*.pyd"
    ):
        for file in glob.glob(file_pattern):
            os.remove(file)
    for dir_pattern in "Release":
        for dir in glob.glob(dir_pattern):
            shutil.rmtree(dir)


def print_banner(msg):
    # print("==================================================")
    print("= {} ".format(msg))


@invoke.task()
def build_functions(c, path=None):
    """ Build the shared library for the C code """
    c: invoke.Context
    if on_win:
        if not path:
            print("Path is missing")
        else:
            # Using c.cd didn't work with paths that have spaces :/
            path = f'"{path}vcvars32.bat" x86'  # Enter the VS venv
            path += f'&& cd "{os.getcwd()}"'  # Change to current dir
            path += "&& cl /LD functions.c"  # Compile
            # Uncomment line below, to suppress stdout
            # path = path.replace("&&", " >nul &&") + " >nul"
            c.run(path)
    else:
        print_banner("Building C Library (comment this msg in tasks.py)")
        cmd = "gcc -c -Wall -Werror -fpic functions.c -I /usr/include/python3.7"
        invoke.run(cmd)
        invoke.run("gcc -shared -o libfunctions.so functions.o")
        print("* Complete  (comment this msg in tasks.py) \n")


@invoke.task()
def test_ctypes(c):
    """ Run the script to test ctypes """
    # print_banner("Testing ctypes Module")
    if on_win:
        invoke.run("python ctypes_test.py")
    else:
        invoke.run("python3 ctypes_test.py", pty=True)


@invoke.task(
    clean,
    build_functions,
    test_ctypes
)
def all(c):
    """ Build and run all tests """
    pass
