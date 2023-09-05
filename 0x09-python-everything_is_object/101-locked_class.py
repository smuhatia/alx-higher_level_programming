#!/usr/bin/python3
"""locked class with no class or attribute"""


class LockedClass:
    """locked class"""
    def __setattr__(self, name, value):
        if name != "first_name":
            msg = "'LockedClass' object has no attribute 'last_name'"
            raise AttributeError(msg)
            self.__dict__[name] = value
