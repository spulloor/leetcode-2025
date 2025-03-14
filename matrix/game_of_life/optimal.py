import copy
from typing import List

import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        cp = copy.deepcopy(board)
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):

                cnt = 0

                # top left
                if i - 1 >= 0 and j - 1 >= 0:
                    if board[i - 1][j - 1] == 1:
                        cnt += 1

                # top
                if i - 1 >= 0:
                    if board[i - 1][j] == 1:
                        cnt += 1

                # top right
                if i - 1 >= 0 and j + 1 < len(board[0]):
                    if board[i - 1][j + 1] == 1:
                        cnt += 1

                # left
                if j - 1 >= 0:
                    if board[i][j - 1] == 1:
                        cnt += 1

                # right
                if j + 1 < len(board[0]):
                    if board[i][j + 1] == 1:
                        cnt += 1

                # bottom left
                if i + 1 < len(board) and j - 1 >= 0:
                    if board[i + 1][j - 1] == 1:
                        cnt += 1

                # bottom
                if i + 1 < len(board):
                    if board[i + 1][j] == 1:
                        cnt += 1

                # bottom right
                if i + 1 < len(board) and j + 1 < len(board[0]):
                    if board[i + 1][j + 1] == 1:
                        cnt += 1

                if board[i][j] == 1:

                    if not cnt in [2, 3]:
                        cp[i][j] = 0

                else:
                   if cnt == 3:
                        cp[i][j] = 1

        # set the board to the copy
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = cp[i][j]

                

        

Solution.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])