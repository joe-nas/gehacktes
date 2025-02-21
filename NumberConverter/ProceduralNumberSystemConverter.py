# from the string module, import an object which contains an ordered list of uppercase letters
from string import ascii_uppercase
from functools import reduce

# construct a hex to decimal lookup table/dict

# creates a list with decimal numbers 0...15
# https://www.w3schools.com/python/python_lists_comprehension.asp
decimal = [x for x in range(0, 36)]

# similarly creates a list with the corresponding hex values from 0...9 and A-F
hexadecimal = [str(x) for x in range(0, 10)] + [x for x in ascii_uppercase]

# create tuples using zip() for key and value pairs e.g. (1,1) ... (Z,35)
# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/ref_func_zip.asp
# https://www.w3schools.com/python/python_dictionaries.asp
hexLookUpDict = dict(zip(hexadecimal, decimal))
# using this construct it is easy to look up the decimal number for any

# def fromBaseToDecimalConversion(from_number, from_base):
#     power = len(from_number) - 1
#     to_number = 0

#     for n in from_number:
#         to_number += int(hexLookUpDict.get(n)) * (from_base**power)
#         power -= 1
#     # print(f"{from_number} in base {from_base} system converts to decimal: {to_number}")
#     return to_number


# def fromDecimalToBase(from_number, to_base):
#     rest = from_number
#     to_number = ""
#     while rest > 0:
#         # rest
#         to_number += str(rest % to_base)
#         rest = rest // to_base

#     to_number = to_number[::-1]
#     print(f"decimal {from_number} converts to {to_number} in base {to_base} system")
#     return to_number
