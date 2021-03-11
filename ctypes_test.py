#!/usr/bin/env python
""" Simple examples of calling C functions through ctypes module. """
import ctypes
from ctypes import Structure, c_char_p, c_int, c_float, c_double, byref, POINTER
import sys
import os

class MyStruct(Structure):
    _fields_ =[("name",c_char_p),
               ("age",c_int),
               ("mark",c_double)
               ]

# Load the shared library into C types.
if __name__ == "__main__":
    if sys.platform.startswith("win"):
        c_lib = ctypes.CDLL("functions.dll")
    else:
        cur_path = os.getcwd()
        lib_path = os.path.join (cur_path, "libfunctions.so")
        c_lib = ctypes.CDLL(lib_path)

    print("=================================")

    # Sample data
    x, y = 5, 3.3

    # You need tell ctypes that the function returns a float (if the function return is different than integer)
    c_lib.cmult.restype = c_float

    # Example of numeric functions
    r1 = c_lib.cmult(x, c_float(y))
    r2 = c_lib.csum(2,5)
    print("Python program : variable r2 contains result from csum", r2)

    print("\n=================================")

    # Example of array type function
    a = (c_int * 3) (-1,  2 ,  5)
    f_arr = c_lib.cfun_array
    f_arr.restype = POINTER(c_int * 3)
    print("Python program : previous array: ", [i for i in a])
    print ("Python program : new array: ", [i for i in f_arr(a).contents])

    print("\n=================================")

    # Example of struct type function
    st = MyStruct(c_char_p(b"Manolo"), 37, 6.8)
    result = c_lib.comprobar_num

    #Sending and receiving pointers
    result.restype = POINTER(MyStruct)
    output  = result(byref(st))
    
    # Getting content from pointer
    final_output = output.contents
    print("Python program : ", final_output.name.decode(), ", ", final_output.age, ", ", final_output.mark)

    print("\n=================================")
