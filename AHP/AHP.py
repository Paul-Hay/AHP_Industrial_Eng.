# ----------- IMPORTING PYTHON MODULES --------#
import numpy as np
import alternatives
import criteria

#------------ DECLARING VARIABLES -------------#

# Defining the criteria and alternatives
criteria_list = criteria.criteria_list
alternative_list = []
# Setting the acceptable threshold for consistency ratio (CR)
threshold = 0.1

#------------ FUNCTIONS -------------#

# Defining a function to calculate priority vectors
def calculate_priority_vector(matrix):

    # Calculate the column-wise normalized matrix
    column_sum = matrix.sum(axis=0, keepdims=True)
    normalized_matrix = matrix / column_sum

    # Calculate the weights (priority vector) for each criterion/alternative
    weights = normalized_matrix.mean(axis=1)
    return weights

# Defining a function to do special multiplication and sum (Refer to formula)
def multiply_and_add(row_matrix, matrix):
    n = len(row_matrix)
    if n != matrix.shape[1]:
        raise ValueError("Number of elements in the row matrix must match the number of columns in the square matrix.")

    vector = np.zeros((1,matrix.shape[0]))
    
    for i in range(n):
        row_element = row_matrix[i]
        matrix_column = matrix[:,i]
        v = row_element*matrix_column
        vector = vector + v

    return vector

# Defining function to select appropriate random index
def random_index_value(case):
    if case == 1:
        return 0
    elif case == 2:
        return 0
    elif case == 3:
        return 0.58
    elif case == 4:
        return 0.90
    elif case == 5:
        return 1.12
    elif case == 6:
        return 1.24
    elif case == 7:
        return 1.32
    elif case == 8:
        return 1.41
    elif case == 9:
        return 1.45
    elif case == 10:
        return 1.49
    else:
        return 0

# Defining a Function to calculate consistency ratio
def consistency_ratio(matrix):
    new_vector  = multiply_and_add(calculate_priority_vector(matrix), matrix)/calculate_priority_vector(matrix)
    lambda_max = new_vector.mean(axis= 1)

    n = len(matrix)
    consistency_index = (lambda_max - n) / (n - 1)
    
    # Consistency Index (CI) should be calculated using the random index for n x n matrices.
    # For n=5, the random index is 1.12.
    random_index = random_index_value(n)
    consistency_ratio = consistency_index / random_index
    return consistency_ratio


#------------ TAKING USER INPUTS -------------#

#-------- Pairwise comparison matrix for criteria ---------#
# Taking user inputs for Criteria Pairwise Comparison Matrix
criteria_matrix = criteria.get_square_matrix()
print("\nCriteria Pairwise Comparison Matrix:")
print(criteria_matrix)

#---------- Pairwise comparison matrix for alternatives for each criterion ---------#

# Taking user inputs for Alternatives Pairwise Comparison Matrix for each criteria
try:
    num_arrays = len(criteria_matrix)
    array_size = int(input("\nEnter the number alternatives you want to input: "))
    if num_arrays <= 0:
        raise ValueError("Number of alternatives should be a positive integer.")
    
    for i in range(num_arrays):
            alternative_list.append("Alternative {}".format(i+1))

    alternative_matrices = alternatives.get_square_arrays(num_arrays, array_size)
    print("\nAlternatives Pairwise Comparison for each Criterion Matrix:")
    print(alternative_matrices)
except ValueError as ve:
    print(ve)



#-------- PRIORITY VECTORS ---------#

# Calculate the priority vector for criteria
criteria_priority_vector = calculate_priority_vector(criteria_matrix)

# Calculate the priority vector for alternatives for each criteria
alternatives_priority_vectors = [calculate_priority_vector(matrix) for matrix in alternative_matrices]


#--------- CONSISTENCY CHECK ---------#

# Calculating Consistency Ratio for criteria
criteria_CR = consistency_ratio(criteria_matrix)
# Calculating Consistency Ratio for each alternatives
alternative_CRs = [consistency_ratio(matrix) for matrix in alternative_matrices]

# Checking if the consistency ratios are within the acceptable range
print("\nCriteria Consistency Ratio: {}".format(criteria_CR))
for i, cr in enumerate(alternative_CRs):
    print("\nAlternative {} Consistency Ratio:".format(i+1), cr) 

if criteria_CR > threshold or any(cr > threshold for cr in alternative_CRs):
    print("\nInconsistent comparison matrices! Please review your pairwise comparisons.")
else:
    print("\nConsistency check passed. Continuing with the AHP calculation...")


#--------- OVERALL PRIORITY VECTOR  -----------# 
alternatives_priority_vectors = np.stack(alternatives_priority_vectors).transpose()

overall_priority_vector = multiply_and_add(criteria_priority_vector, alternatives_priority_vectors)

overall_priority_vector = np.squeeze(overall_priority_vector)

#--------- RANKING THE OVERALL PRIORITY VECTOR  -----------# 
ranking = np.argsort(overall_priority_vector, kind='quicksort')[::-1]

#--------- OUTPUT DISPLAY  -----------# 

print("\nCriteria priority vector: {}".format(criteria_priority_vector))
print("\nAlternative priority vectors for each criteria:")
for i, alt_weights in enumerate(alternatives_priority_vectors):
    print(f"{alternative_list[i]}:", alt_weights)

print("\nOverall priority vector: {}".format(overall_priority_vector))

print("\nRanked alternatives by overall performance scores:")
for i, rank in enumerate(ranking, 1):
    print(f"{i}. {alternative_list[rank]}")

print(f"\nThe AHP analysis shows that alternative {alternative_list[ranking[0]]} is the best choice")
