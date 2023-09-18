# This code is used to take user inputs for Criteria Peacewise Comparison Matrix

import numpy as np

criteria_list = []

def get_square_matrix():
    while True:
        try:
            # Get the dimensions of the square matrix from the user
            n = int(input("Enter the number of criteria: "))
            if n <= 0:
                raise ValueError("Size should be a positive integer.")
            break
        except ValueError as ve:
            print(ve)

    for i in range(n):
        criteria_list.append("Criteria {}".format(i+1))

    matrix_elements = []
    print("Enter the Numerical Rating of the Pairwise Comparison Criteria matrix row-wise:")
    print("(Hint: Seperate each matrix element by a single space and use enter key to move on to next row)")
    # Get input for each element of the matrix
    for i in range(n):
        while True:
            try:
                row_input = input().split()
                if len(row_input) != n:
                    raise ValueError(f"Expected {n} elements for row {i+1}.")
                matrix_elements.append([eval(x) for x in row_input])
                break
            except ValueError as ve:
                print(ve)

    # Convert the input into a NumPy array
    square_matrix = np.array(matrix_elements)

    return square_matrix
