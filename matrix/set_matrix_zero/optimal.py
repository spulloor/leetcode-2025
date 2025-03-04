from typing import List


class Solution:
    @staticmethod
    def setZeroes(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # tag the positions that need to be zero
        rows, cols = len(matrix), len(matrix[0])

        rowZero = False

        # loop through the matrix and set the first row and first col for the rth and cth rows and columns
        for i in range(rows):
            for j in range(cols):

                if matrix[i][j] == 0:

                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
                    
                    matrix[0][j] = 0

        # set all the rows and cols to zero expect the first ones
        for i in range(1, rows):
            for j in range(1, cols):

                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # now loop through the first row
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0

        # now loop through the first col
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0



        
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Solution.setZeroes([[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]) 