#!/usr/bin/python3
def divisible_by_2(my_list):
    new_list = [integer % 2 == 0 for integer in my_list]
    return new_list

