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


# def recursiveFromBaseToDecimalConversion(from_number_str, from_base, to_number):
def recursiveFromBaseToDecimalConversion(from_number_str, from_base, accumulator=0):
    power = len(str(from_number_str)) - 1

    # base_case, function execution stops, converges when power of 0 is reached
    if power == 0:

        return (
            accumulator + int(hexLookUpDict.get(from_number_str[0])) * from_base**power
        )

    return recursiveFromBaseToDecimalConversion(
        from_number_str[1::],
        from_base,
        # add base to decimal calculation: n * base ** power
        accumulator + hexLookUpDict.get(from_number_str[0]) * from_base**power,
    )


def recursiveFromDecimalToBase(from_number, to_base, acummulator=[]):
    # def recursiveFromDecimalToBase(from_number, to_base, to_number=[]):
    rest = from_number

    # base case
    if rest == 0:
        return int(reduce(lambda x, y: x + y, acummulator))

    acummulator.insert(0, str(rest % to_base))
    rest = rest // to_base

    # print(f"to_number: {acummulator}, rest: {rest}")

    return recursiveFromDecimalToBase(rest, to_base, acummulator)


def combinedRecursiveConversion(from_number, from_base, to_base):
    intermediary_dec = recursiveFromBaseToDecimalConversion(from_number, from_base)
    return recursiveFromDecimalToBase(intermediary_dec, to_base)
