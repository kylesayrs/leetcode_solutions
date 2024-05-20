from typing import List

import math


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Use matrix as cache
        """
        n = len(matrix)
        # assert n >= 1
        # assert len(matrix) == len(matrix[0])

        # recursion
        for row in reversed(range(n - 1)):
            for col in range(n):
                matrix[row][col] += min(
                    matrix[row + 1][col - 1] if col - 1 >= 0 else math.inf,
                    matrix[row + 1][col],
                    matrix[row + 1][col + 1] if col + 1 < n else math.inf
                )

        # pick min start
        return min(matrix[0])


if __name__ == "__main__":
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    print(Solution().minFallingPathSum(matrix))
