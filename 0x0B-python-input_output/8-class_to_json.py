#!/usr/bin/python3
""" a dict description for JSON serialization"""


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure"""
    return (obj.__dict__)
