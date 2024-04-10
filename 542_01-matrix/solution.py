from typing import List

import math
import numpy
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])

        update_matrix = [[math.inf for _ in range(width)] for _ in range(height)]
        queue = deque()

        # queue 0s
        for row in range(height):
            for column in range(width):
                if mat[row][column] == 0:
                    queue.append((row, column))

        # bfs
        while len(queue) > 0:
            row, column = queue.popleft()

            # oob condition
            if (
                row < 0 or row >= height or
                column < 0 or column >= width
            ):
                continue

            # seen condition
            if update_matrix[row][column] != math.inf:
                continue

            # process
            if mat[row][column] == 0:
                update_matrix[row][column] = 0
            
            else:
                update_matrix[row][column] = min(
                    update_matrix[row - 1][column] if row > 0 else math.inf,
                    update_matrix[row + 1][column] if row < height - 1 else math.inf,
                    update_matrix[row][column - 1] if column > 0 else math.inf,
                    update_matrix[row][column + 1] if column < width - 1 else math.inf,
                ) + 1

            # recurse
            queue.append((row - 1, column))
            queue.append((row + 1, column))
            queue.append((row, column - 1))
            queue.append((row, column + 1))

        return update_matrix


if __name__ == "__main__":
    assert Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
    assert Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]
    assert Solution().updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]) == [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
    assert Solution().updateMatrix([[1,0,0],[1,1,1],[1,1,1]]) == [[1,0,0],[2,1,1],[3,2,2]]
