#!/usr/bin/python3

def uppercase(str):
    string = ""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            character = chr(ord(c) - 32)
            string += character
        else:
            string += c
print("{}".format(string))
