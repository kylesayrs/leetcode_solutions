from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for index in range(1, len(points)):
            x_difference = abs(points[index][0] - points[index - 1][0])
            y_difference = abs(points[index][1] - points[index - 1][1])

            diagonal_side_len = min(x_difference, y_difference)
            
            total += diagonal_side_len
            total += max(x_difference, y_difference) - diagonal_side_len

        return total
