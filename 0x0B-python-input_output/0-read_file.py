#!/usr/bin/python3
""" Read from a file"""


def read_file(filename=""):
    """ Reads text froma file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
