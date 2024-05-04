from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        remainders = [0, 0, 0]
        for num in nums:
            for remainder in remainders[:]:
                remainders[(num + remainder) % 3] = max(remainders[(num + remainder) % 3], num + remainder)
        return remainders[0]
