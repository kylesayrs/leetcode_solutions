from typing import List

import math


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            # bias left arbitrarily
            middle = (right - left) // 2 + left

            left_element = (
                nums[middle - 1]
                if middle - 1 >= 0
                else -math.inf
            )

            right_element = (
                nums[middle + 1]
                if middle + 1 <= len(nums) - 1
                else -math.inf
            )

            # left boundary
            if middle == 0:
                if right_element < nums[middle]:
                    return middle

                left = middle + 1
                continue
                
            # right boundary
            if middle == len(nums) - 1:
                if left_element < nums[middle]:
                    return middle
                
                right = middle
                continue

            # if peak
            if left_element < nums[middle] and right_element < nums[middle]:
                return middle
                
            if left_element < nums[middle]:
                left = middle + 1
            else:
                right = middle

        assert left == right
        return left
    

if __name__ == "__main__":
    assert Solution().findPeakElement([1, 2, 3]) == 2
    assert Solution().findPeakElement([1, 5, 3]) == 1
    assert Solution().findPeakElement([7, 5, 3]) == 0
    assert Solution().findPeakElement([7, 5, 3, 1, 1, 1]) == 0
