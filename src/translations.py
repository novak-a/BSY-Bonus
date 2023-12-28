#
# Author: Adam Novak
#
# Plagiarism is a sin!
# Plagiarism is a sin!
# Plagiarism is a sin!
#

import base64


DICTIONARY = {
    "A": "Apple",
    "B": "Banana",
    "C": "Cat",
    "D": "Dog",
    "E": "Elephant",
    "F": "Fish",
    "G": "Grape",
    "H": "Hat",
    "I": "Ice Cream",
    "J": "Jacket",
    "K": "Kangaroo",
    "L": "Lemon",
    "M": "Monkey",
    "N": "Notebook",
    "O": "Orange",
    "P": "Penguin",
    "Q": "Queen",
    "R": "Rabbit",
    "S": "Snake",
    "T": "Tree",
    "U": "Umbrella",
    "V": "Violet",
    "W": "Watermelon",
    "X": "Xylophone",
    "Y": "Yellow",
    "Z": "Zebra",
    "a": "apple",
    "b": "banana",
    "c": "cat",
    "d": "dog",
    "e": "elephant",
    "f": "fish",
    "g": "grape",
    "h": "hat",
    "i": "ice cream",
    "j": "jacket",
    "k": "kangaroo",
    "l": "lemon",
    "m": "monkey",
    "n": "notebook",
    "o": "orange",
    "p": "penguin",
    "q": "queen",
    "r": "rabbit",
    "s": "snake",
    "t": "tree",
    "u": "umbrella",
    "v": "violet",
    "w": "watermelon",
    "x": "xylophone",
    "y": "yellow",
    "z": "zebra",
    "+": "plus",
    "/": "slash",
    "=": "="
}

SWITCHED_DICTIONARY = {
    value: key for key, value in DICTIONARY.items()
}


def encode_string(input_string):
    encoded_data = base64.b64encode(input_string.encode('utf-8')).decode('utf-8')
    result = []
    for char in encoded_data:
        if char in DICTIONARY:
            result.append(DICTIONARY[char])
        else:
            result.append(char)
    return " ".join(result)


def decode_string(input_string):
    result = []
    words = input_string.split()
    for word in words:
        result.append(SWITCHED_DICTIONARY.get(word, word))
    decoded_data = base64.b64decode("".join(result))
    return decoded_data.decode('utf-8')
