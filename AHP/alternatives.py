
# This code is used to take user inputs for Alternatives Peacewise Comparison Matrix for each Criteria
import numpy as np

def get_square_arrays(num_arrays, array_size):
    array_list = []
    for i in range(num_arrays):
        print(f"Enter the Numerical Ratings for Pairwise Comparison Alternatives Matrix under Criterion {i+1} row-wise (Size: {array_size}x{array_size}):")
        print("(Hint: Seperate each matrix element by a single space and use enter key to move on to next row)")
        array_elements = []
        for j in range(array_size):
            while True:
                try:
                    row_input = input().split()
                    if len(row_input) != array_size:
                        raise ValueError(f"Expected {array_size} elements for row {j+1}.")
                    array_elements.append([eval(x) for x in row_input])
                    break
                except ValueError as ve:
                    print(ve)
        array = np.array(array_elements)
        array_list.append(array)

    square_arrays = np.stack(array_list)

    return square_arrays