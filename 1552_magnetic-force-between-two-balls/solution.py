from typing import List


class Solution:
    @staticmethod
    def feasible(min_force: int, position: List[int], m: int):
        prev_ball = None

        num_balls_placed = 0
        for p in position:
            if prev_ball is None or p - prev_ball >= min_force:
                prev_ball = p
                num_balls_placed += 1

        return num_balls_placed >= m
    

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        #assert len(position) > 0

        left = 1
        right = position[-1]
        max_min_force = -1
        while (left < right):
            min_force_candidate = (right - left) // 2 + left

            if Solution.feasible(min_force_candidate, position, m):
                left = min_force_candidate + 1
                max_min_force = min_force_candidate

            else:
                right = min_force_candidate

        #assert left == right
        return max_min_force
 
