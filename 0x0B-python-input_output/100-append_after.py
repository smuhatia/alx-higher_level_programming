#!/usr/bin/python3
"""a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename, search_string, new_string):
    """inserts a line of text to a file"""
    text = []
    with open(filename, 'r+', encoding='utf-8') as fw:
        text = file.readlines()

    with open(filename, 'w', encoding='utf-8') as fw:
        for lines in text:
            fw.write(lines)

            if search_string in lines:
                fw.write(new_string)
