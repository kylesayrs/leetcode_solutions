from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta_nums = [(num ^ k) - num for num in nums]
        delta_nums = list(reversed(sorted(delta_nums)))

        index = 0
        max_sum = sum(nums)
        while index + 1 < len(delta_nums):
            toggle_delta = delta_nums[index] + delta_nums[index + 1]

            if toggle_delta <= 0:
                index += 1

            else:
                max_sum += toggle_delta
                index += 2

        return max_sum
