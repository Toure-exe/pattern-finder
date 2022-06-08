# Project by Lorenzo Camilleri - Giulio Taralli - Ismaila Toure
import numpy as np

# Method which creates a random matrix composed of 1 and 0 and based on the number of rows and columns.
def create_matrix(m, n):
    return np.random.randint(2, size=(m, n))  # First number = range; Second number = row + column size.


# method used in the GUI to color the matrix cells were the pattern has been found
def in_range(i, j, i_start, j_start, i_end, j_end):  # check if the cell of the matrix we are showing is in the range of the pattern previously found
    if i_start <= i <= i_end and j_start <= j <= j_end:
        return True
    return False


def ContinSubSeq(lst):
    size = len(lst)
    for start in range(size):
        for end in range(start + 1, size + 1):
            yield (start, end)


# Method which divides the matrix into submatrixes, this method just create 1 submatrix which return you a tuple with
# the following informations [matrix, start_row, start_col, end_row-1, end_col-1] This method just returns you 1
# submatrixes, it will indeed be called in the method get_all_sub_mat() in order to add every submatrix into the list
# of all the submatrixes.
def getsubmat(mat, start_row, end_row, start_col, end_col):
    matrix = []
    # print("------------------------------------")
    # print("mat is \n", mat)
    for i in mat[start_row:end_row]:
        matrix.append(list(i[start_col:end_col]))
    result = (matrix, start_row, start_col, end_row - 1, end_col - 1)
    return result


# Method which checks if the pattern/colums of the pattern are the same of the submatrix, this method is very useful
# in terms of algorithm complexity. We want to add into the list of submatrix just the sub matrix with same dimension
# of the pattern itself, the reason is the same as check_if_comparable() method. In this way we will do less useless
# matrix comparisons and the time complexity will be lower.
def check_if_same_dimension(pattern_rows, pattern_cols, sub_mat_row, sub_mat_col):
    return pattern_rows == sub_mat_row and pattern_cols == sub_mat_col


# Method which gives the list of the submatrixes of the matrix given, it uses the method getsubmat() and it will add
# each submatrix everytime in order to make a list ( all of them are tuple like we mentioned in the method before).
def get_all_sub_mat(mat, pattern_rows, pattern_cols):
    rows = len(mat)
    cols = len(mat[0])
    list_of_sub_mat = []
    for start_row, end_row in ContinSubSeq(list(range(rows))):
        for start_col, end_col in ContinSubSeq(list(range(cols))):
            if not (start_col == end_col - 1 and start_row == end_row - 1) and check_if_same_dimension(pattern_rows,
                                                                                                       pattern_cols,
                                                                                                       end_row - start_row,
                                                                                                       end_col - start_col):  # Exclude all pattern with single cell value ( we assume is not a pattern).
                sub_mat = getsubmat(mat, start_row, end_row, start_col, end_col)
                list_of_sub_mat.append(sub_mat)

    # print("---------------------------------------")
    # print(list_of_sub_mat)
    return list_of_sub_mat


def compare_matrixes(sub_matrix, pattern):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i][j] != sub_matrix[i][j]:
                return False
    return True


# method to create a colored matrix for the GUI by using matplotlib
# and a 3d_matrix to color and then insert the values.
def create_colored_matrix(list_of_matches, matrix, ax):
    white = np.array([255, 255, 255])
    red = np.array([255, 0, 0])
    matrix_3d = np.ndarray(shape=(matrix.shape[0], matrix.shape[1], 3), dtype=int)

    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            matrix_3d[i][j] = np.array([255, 255, 255])  # white

    if len(list_of_matches) > 0:  # if we found matches we need to draw, else we does not.
        for match in list_of_matches:
            for i in range(0, matrix.shape[0]):
                for j in range(0, matrix.shape[1]):
                    if in_range(i, j, match[0], match[1], match[2], match[3]):
                        print("true with i: ", i, " and j: ", j)
                        matrix_3d[i][j] = red  # red if in the range of pattern found coordinates
                    else:
                        if not np.array_equal(matrix_3d[i][j], red):
                            matrix_3d[i][j] = white  # white otherwise
    else:
        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]):
                matrix_3d[i][j] = np.array([255, 255, 255])  # white

    ax.matshow(matrix_3d)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            c = matrix[j, i]
            ax.text(i, j, "", va='center', ha='center')
            ax.text(i, j, str(c), va='center', ha='center')