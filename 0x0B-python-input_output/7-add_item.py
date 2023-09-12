#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a JSON file."""

# Import necessary modules
import sys

if __name__ == "__main__":
    # Import the required functions from the specified modules
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
            '6-load_from_json_file').load_from_json_file

    # Define the filename for the JSON file
    filename = "add_item.json"

    # Get all command-line arguments excluding the script name itself
    arguments = sys.argv[1:]

    # Try to load the existing list from the file
    # If the file doesn't exist (causing a FileNotFoundError)
    # initialize an empty list
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    # Extend the list with the new arguments
    items.extend(arguments)

    # Save the updated list back to the file
    save_to_json_file(items, filename)
