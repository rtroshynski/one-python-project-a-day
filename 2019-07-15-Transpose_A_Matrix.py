# Python Program - Find Transpose of a Matrix
# https://codescracker.com/python/program/python-program-transpose-matrix.htm
matrix = [[1, 2],
	  [3, 4],
	  [5, 6]]
rmatrix = [[0, 0, 0],
	   [0, 0, 0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        rmatrix[j][i] = matrix[i][j]
for r in rmatrix:
    print(r)
# eof
