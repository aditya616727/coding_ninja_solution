
from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    row =len(matrix)
    column = len(matrix[0])
    zero_rows, zero_column = set(),set()
    for i in range(row):
        for j in range(column):
            if matrix[i][j] ==0:
                zero_rows.add(i)
                zero_column.add(j)
    for i in range(row):
        for j in range(column):
            if i in zero_rows or j in zero_column:
                matrix[i][j] =0
    return matrix # type: ignore

    pass