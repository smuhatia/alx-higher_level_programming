#!/usr/bin/python3
"""
This code generates Pascal's triangle by first creating an empty list
for each row, then filling in the values for each element in the row
based on the values in the previous row. The first and last elements
of each row are always 1, and the other elements are calculated as the
sum of the two elements directly above them in the triangle. The triangle
is then printed with leading spaces to align the rows correctly.
"""


def pascal_triangle(n):
    """ pascal's triangle"""
    # If n <= 0, return an empty list
    if n <= 0:
        return []

    # Initialize our triangle with the first row
    triangle = [[1]]

    # Generate the rest of the rows
    for i in range(1, n):
        last_row = triangle[-1]  # Get the last row
        # Create new row. Start and end with a '1'
        # sum of the two numbers above it, i.e., from last_row
        new_row = [1] + [last_row[j-1] + last_row[j]
                         for j in range(1, i)] + [1]
        # Add this row to our triangle
        triangle.append(new_row)

    return triangle
