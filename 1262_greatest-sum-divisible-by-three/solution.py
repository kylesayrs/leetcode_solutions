from typing import List

import math


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        max_sum_with_remainder = [0, -math.inf, -math.inf]

        for num in nums:
            # max for each remainder if number is included
            include_maxes = [
                max_sum_with_remainder[(remainder - num) % 3] + num
                for remainder in range(3)
            ]

            max_sum_with_remainder = [
                max(max_sum_with_remainder[remainder], include_maxes[remainder])
                for remainder in range(3)
            ]
        
        return max_sum_with_remainder[0]


if __name__ == "__main__":
    assert Solution().maxSumDivThree([1, 2, 3, 4, 5]) == 15
    assert Solution().maxSumDivThree([3,6,5,1,8]) == 18
    assert Solution().maxSumDivThree([1,2,3,4,4]) == 12
