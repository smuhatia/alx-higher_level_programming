#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
    for new_list in my_list:
        print("{:d}".format(new_list))
