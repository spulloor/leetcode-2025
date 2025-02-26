from typing import List

class Solution:

    @staticmethod
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        res = []

        while left < right and top < bottom:

            # loop through left to right
            for col in range(left, right):
                res.append(matrix[top][col])

            # increment top
            top += 1

            # loop through top to bottom
            for row in range(top, bottom):
                res.append(matrix[row][right - 1])

            right -= 1

            if not (left < right and top < bottom):
                break

            # loop through right to left
            for col in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][col])

            bottom -= 1

            # loop through bottom to top
            for row in range(bottom - 1, top - 1, -1):
                res.append(matrix[row][left])

            left += 1

        return res
        
        
        

#Solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) # [1,2,3,6,9,8,7,4,5]
Solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # [1,2,3,4,8,12,11,10,9,5,6,7]
Solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) # [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
Solution.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]) # [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]