from random import randrange
from string import ascii_uppercase
from functools import reduce
import os

file_name = "loremIpsum.txt"
os.chdir("myencryption")
with open(file_name, "r") as file:
    message = file.read().upper().replace(" ", "_")

letters = (
    [str(x) for x in range(0, 10)]
    + [x for x in ascii_uppercase]
    + [".", ",", "!", "?", "_"]
)

encoder_str = reduce(lambda x, y: x + y, letters)


def textEncoding(message, encoder):
    # using list comprehensions
    # return [encoder.index(letter) for letter in message]

    message_encoded = []
    for char in message:
        message_encoded.append(encoder.index(char))

    return message_encoded


# def createKeysAdvanced(encoded_message):
# benutzt list comprehensions, sowie zip und unpack
# https://book.pythontips.com/en/latest/zip.html
#     def keyGen(number):
#         k1 = number - randrange(0, number + 1)
#         k2 = number - k1
#         return (k1, k2)

#     keys = [keyGen(x) for x in encoded_message]
#     k1, k2 = zip(*keys)
#     return (k1, k2)


def createKeys(encoded_message):
    def keyGen(number):
        k1 = number - randrange(0, number + 1)
        k2 = number - k1
        return (k1, k2)

    keys1 = []
    keys2 = []

    for number in encoded_message:
        key1, key2 = keyGen(number)
        keys1.append(key1)
        keys2.append(key2)

    return (keys1, keys2)


# def decryptMessageAdvanced1(encoder_str, key1, key2):
# gebraucht functional programming map(), reduce() framework, list comprehensions, sowie lambda funtions
#     message = [encoder_str[x] for x in map(lambda k1, k2: k1 + k2, key1, key2)]
#     return reduce(lambda a, b: a + b, message)


# def decryptMessageAdvanced1(encoder_str, key1, key2):
#     message = ""
#     for k1, k2 in zip(key1, key2):
#         message += encoder_str[k1 + k2]

#     return message


def decryptMessage(encoder_str, key1, key2):
    message = ""
    message_length = len(key1)

    for i in range(0, message_length):
        message += encoder_str[key1[i] + key2[i]]

    return message


message_encoded = textEncoding("HALLO123_", encoder_str)
print(message_encoded)
key1, key2 = createKeys(message_encoded)

print(decryptMessage(encoder_str, key1, key2))
