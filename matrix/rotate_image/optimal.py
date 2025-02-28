from typing import List

class Solution:
    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        l, r = 0, len(matrix) - 1
        t, b = 0, len(matrix) - 1

        while l < r:


            for i in range(r - l):

                topLeft = matrix[t][l + i]

                matrix[t][l + i] = matrix[b - i][l]

                matrix[b - i][l] = matrix[b][r - i]

                matrix[b][r - i] = matrix[t + i][r]

                matrix[t + i][r] = topLeft

            l += 1
            r -= 1
            t += 1
            b -= 1


        
#Solution.rotate([[1,2,3],[4,5,6],[7,8,9]])
Solution.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) # [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
