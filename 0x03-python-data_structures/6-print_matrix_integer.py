#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    max_width = max(len(str(num)) for row in matrix for num in row)

    for row in matrix:
        for num in row:
            print("{:>{width}}".format(num, width=max_width), end=" ")
        print("$")

    print("$")  #
