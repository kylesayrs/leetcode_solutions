from typing import List

import math


class Solution:
    def findMax(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            # bias right since we're looking for a max
            # if left and right are one apart, we want to check right first
            middle = math.ceil((right - left) / 2) + left
            
            # out of order, max must be inbetween
            # since we biased right, we need to subtract one to right to avoid
            # the infinite condition M == R
            if nums[left] > nums[middle]:
                right = middle - 1

            # out of order, max must be inbetween
            elif nums[right] < nums[middle]:
                left = middle

            # if numbers are ascending between left and right, then search right
            else:
                left = middle

        assert left == right
        return nums[left]
                
        

if __name__ == "__main__":
    assert Solution().findMax([0, 1, 2]) == 2
    assert Solution().findMax([2, 0, 1]) == 2
    assert Solution().findMax([1, 2, 0]) == 2

    assert Solution().findMax([3,4,5,1,2]) == 5
    assert Solution().findMax([4,5,6,7,0,1,2]) == 7
    assert Solution().findMax([11,13,15,17]) == 17
