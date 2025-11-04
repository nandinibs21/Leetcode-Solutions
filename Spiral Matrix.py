class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            # take first row
            res += matrix.pop(0)
            # take last element of remaining rows
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            # take last row reversed
            if matrix:
                res += matrix.pop()[::-1]
            # take first element of remaining rows (bottom to top)
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res
