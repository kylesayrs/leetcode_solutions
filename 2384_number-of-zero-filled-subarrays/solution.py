from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0

        left = -1
        for right in range(len(nums)):
            if nums[right] == 0:
                if left == -1:
                    left = right

            else:
                if left != -1:
                    subarray_len = right - left
                    total += subarray_len * (subarray_len + 1) // 2
                    left = -1

        # end case
        if left != -1:
            subarray_len = len(nums) - left
            total += subarray_len * (subarray_len + 1) // 2

        return total
