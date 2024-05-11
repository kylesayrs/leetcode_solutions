from typing import List

import math


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        rearranged = [0 for _ in range(len(nums))]

        half_len = math.ceil(len(nums) / 2)
        lessers = nums[:half_len]
        greaters = nums[half_len:]

        # insert lessers
        for index, num in enumerate(lessers):
            index = (index << 1)
            rearranged[index] = num

        # insert lessers
        for index, num in enumerate(greaters):
            index = (index << 1) + 1
            rearranged[index] = num

        return rearranged
    

if __name__ == "__main__":
    print(Solution().rearrangeArray([1, 2, 3, 4, 5, 6, 7]))
