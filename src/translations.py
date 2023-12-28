#
# Author: Adam Novak
#
# Plagiarism is a sin!
# Plagiarism is a sin!
# Plagiarism is a sin!
#

import base64


DICTIONARY = {
    "0": "Apple",
    "1": "Banana",
    "2": "Cat",
    "3": "Dog",
    "4": "Elephant",
    "5": "Fish",
    "6": "Grape",
    "7": "Hat",
    "8": "Ice",
    "9": "Jacket",
    "a": "Kangaroo",
    "b": "Lemon",
    "c": "Monkey",
    "d": "Notebook",
    "e": "Orange",
    "f": "Penguin",

}

SWITCHED_DICTIONARY = {
    value: key for key, value in DICTIONARY.items()
}


def encode_string(input_string):
    hex_string = input_string.encode('utf-8').hex()
    result = []
    for c in hex_string:
        result.append(DICTIONARY[c])
    return " ".join(result)


def decode_string(input_string):
    hex_string = ""
    for word in input_string.split():
        hex_string += SWITCHED_DICTIONARY[word]
    hex_bytes = bytes.fromhex(hex_string)
    return hex_bytes.decode('utf-8')

