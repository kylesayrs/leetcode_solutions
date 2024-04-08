from typing import List

import math


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        prev_ascending = 0
        prev_descending = 0

        for index in reversed(range(len(nums))):
            can_wiggle = (
                index < len(nums) - 1 and
                nums[index] != nums[index + 1]
            )
            can_wiggle_up = (
                can_wiggle and
                nums[index + 1] > nums[index] 
            )
            can_wiggle_down = (
                can_wiggle and
                nums[index + 1] < nums[index] 
            )

            ascending = max(
                prev_ascending,                                      # continue
                prev_descending + 1 if can_wiggle_up else -math.inf  # wiggle down
            )

            descending = max(
                prev_descending,                                       # continue
                prev_ascending + 1 if can_wiggle_down else -math.inf,  # wiggle up
            )

            prev_ascending = ascending
            prev_descending = descending

        return max(prev_ascending, prev_descending) + 1
    

if __name__ == "__main__":
    assert Solution().wiggleMaxLength([1,2,3]) == 2
    assert Solution().wiggleMaxLength([1,7,4,9,2,5]) == 6
    assert Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7
