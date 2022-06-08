# Project by Lorenzo Camilleri - Giulio Taralli - Ismaila Toure

from utilities.matrix_utils import *
from utilities.rotations import *


# Method which gets the pattern from the file txt, useful for the pattern search.
def get_pattern_from_file():
    data = np.genfromtxt('pattern.txt', dtype=int)
    return data


# Method which checks if the pattern is correct or if you are giving a wrong one based on the number of rows and colums
# This method has been created in order to not have a pattern bigger than the matrix itself or the search can't done.
def check_pattern_is_ok(pattern_rows, pattern_cols, m, n):
    if pattern_rows > m:
        print("Error, the pattern has more rows than the matrix itself.")
        exit(-1)
    if pattern_cols > n:
        print("Error, the pattern has more cols than the matrix itself.")
        exit(-1)


# This is the default pattern search method which checks if there is/are pattern(s) on the matrix.
def normal_pattern_search(list_sub_matrix, pattern):
    list_of_matches = []
    for i in list_sub_matrix:  # (matrix, start_row, start_col, end_row-1, end_col-1)
        sub_matrix = i[0]
        if check_if_comparable(sub_matrix, pattern):  # if the sub_matrix i got is of the same dimension of my pattern
            if compare_matrixes(sub_matrix, pattern):
                print("------------------------------")
                print("Found match with coords after: ")
                print("Start row is: ", i[1])
                print("Start col is: ", i[2])
                print("End row is: ", i[3])
                print("End col is: ", i[4])
                list_of_matches.append((i[1], i[2],i[3],i[4]))


    return list_of_matches


# This is the main pattern search method which will be the one which will search the patterns (with all the rotation + default position) on the matrix-
def find_pattern_in_matrix(pattern, matrix):
    print("Matrix is \n", matrix)
    # IT'S NOT A LIST OF SUBMATRIX, IS A LIST OF TUPLES (SUB_MATRIX, CORD1, CORD2, CORD3, CORD4)
    list_sub_matrix = get_all_sub_mat(matrix, len(pattern), len(pattern[0]))
    found = normal_pattern_search(list_sub_matrix, pattern)
    if len(found) == 0:
        print("No pattern found with no rotation...")
        return []
    else:
        print("list of coords: \n",found)
        return found
    # print("\n")
    # rotation_90_pattern_search(list_sub_matrix, pattern)
    # print("\n")
    # rotation_180_pattern_search(list_sub_matrix, pattern)
    # print("\n")
    # rotation_270_pattern_search(list_sub_matrix, pattern)


# We check if dimension is equal, because there are 2 other cases
#       1) if sub_mat is smaller than pattern you will never find the pattern itself
#       2) if the sub_mat is greater we know that, in the list of sub_mat we got, there is a sub_mat of this sub_mat who dimension is identical to pattern
#          so we won't need to create an harder matrix comparison than the one we do
#       Example:
#           Pattern 1 0              SubMatrix 0 0 1 0 1 1
#                   0 1                        1 1 0 1 0 0
#           We know if the SubMatrix above exists, than our algorithm found another submatrix (sub matrix of this sub matrix) with dimension identical to the
#           dimension of the pattern itself so
#           Sub_Sub_Matrix 1 0
#                          0 1
#           In this way we avoid creating a complicated type of search instead of a O(n^2) matrix comparison
def check_if_comparable(sub_matrix, pattern):
    # print("The submatrix is ", sub_matrix)
    rows_sub_mat = len(sub_matrix)
    cols_sub_mat = len(sub_matrix[0])
    rows_pattern = len(pattern)
    cols_pattern = len(pattern[0])
    if rows_pattern == rows_sub_mat and cols_pattern == cols_sub_mat:
        return True
    else:
        return False


# Method which apply the rotation of the pattern by 90 degree and then it applies the pattern search with the 90 degree pattern.
def rotation_90_pattern_search(list_sub_matrix, pattern):
    print("Rotating pattern by 90 degree...")
    rotated_pattern90 = rotate_pattern90(pattern)
    print("Rotated Pattern is: \n", rotated_pattern90)

    found = normal_pattern_search(list_sub_matrix, pattern)
    if not found:
        print("No pattern found with a 90 degree rotation...")


# Method which apply the rotation of the pattern by 180 degree and then it applies the pattern search with the 180 degree pattern.
def rotation_180_pattern_search(list_sub_matrix, pattern):
    print("Rotating pattern by 180 degree... ")
    rotated_pattern180 = rotate_pattern180(pattern)
    print("Rotated Pattern is: \n", rotated_pattern180)

    found = normal_pattern_search(list_sub_matrix, pattern)
    if not found:
        print("No pattern found with a 180 degree rotation...")


# Method which apply the rotation of the pattern by 270 degree and then it applies the pattern search with the 270 degree pattern.
def rotation_270_pattern_search(list_sub_matrix, pattern):
    print("Rotating pattern 270 degree...")
    rotated_pattern270 = rotate_pattern270(pattern)
    print("Rotated Pattern is: \n", rotated_pattern270)

    found = normal_pattern_search(list_sub_matrix, pattern)
    if not found:
        print("No pattern found with a 270 degree rotation...")


