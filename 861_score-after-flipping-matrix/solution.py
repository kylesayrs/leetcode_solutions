from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)
        score = 0

        # flips rows to maximize most significant figure
        for row in range(height):
            if grid[row][0] != 1:
                grid[row] = [1 - elem for elem in grid[row]]

        # greedly flip columns, prioritizing sig figs
        significance = 1 << (width - 1)
        for col in range(width):
            num_ones = sum(
                grid[row][col]
                for row in range(height)
            )
            num_zeros = height - num_ones

            score += max(num_ones, num_zeros) * significance
            significance = significance >> 1

        return score
