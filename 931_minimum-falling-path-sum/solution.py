from typing import List

import math


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # assert n >= 1
        # assert len(matrix) == len(matrix[0])

        # initialize cache
        cache = [[None for _ in range(n)] for _ in range(n)]

        # initialize last row
        for col in range(n):
            cache[n - 1][col] = matrix[n - 1][col]

        # recursion
        for row in reversed(range(n - 1)):
            for col in range(n):
                cache[row][col] = min(
                    cache[row + 1][col - 1] if col - 1 >= 0 else math.inf,
                    cache[row + 1][col],
                    cache[row + 1][col + 1] if col + 1 < n else math.inf
                ) + matrix[row][col]

        # pick min start
        return min(cache[0])


if __name__ == "__main__":
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    print(Solution().minFallingPathSum(matrix))
