# Project by Lorenzo Camilleri - Giulio Taralli - Ismaila Toure

from utilities.matrix_utils import create_matrix
from utilities.pattern_utils import get_pattern_from_file, check_pattern_is_ok, find_pattern_in_matrix
import time

# This is main file of the project, here you will insert the row and column size, it will then create a random matrix composed of [0,1].
# It will then call a method which will start the pattern search on the matrix.
# The pattern will be searched in its default position, then it will be searched by its rotation of 90 degree, 180 degree and 270 degree.

print("Insert row size here: ")
m = int(input())
print("Insert column size here: ")
n = int(input())
matrix = create_matrix(m, n)
# print(matrix)
print("Taking the pattern from the file...")

pattern = get_pattern_from_file()

print(pattern)
pattern_rows = len(pattern)
pattern_cols = len(pattern[0])

check_pattern_is_ok(pattern_rows, pattern_cols, m, n) # This method breaks the program if the pattern is bigger than the matrix itself.

print("Checking for pattern in matrix")

start_time = time.time()
find_pattern_in_matrix(pattern, matrix)
end_time = time.time()-start_time

print("\nTime spent: ", end_time, "seconds")
# print(matrix)





