from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row has a zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column has a zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Mark rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Use markers to set zeroes
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
