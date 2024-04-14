from typing import List

import math


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        # array is at least length 2
        if len(nums) <= 1:
            return
        
        # find first index where swapping leads to a higher value
        first_swappable_index = len(nums) - 2  # start with second to last
        while first_swappable_index >= 0:
            # since this condition implies that everything to the right is increasing
            # from right to left, we only need to check against the previous value
            if nums[first_swappable_index] < nums[first_swappable_index + 1]:
                break

            first_swappable_index -= 1
        
        # if everything is increasing from right to left, we loop back to the first
        else:
            nums.reverse()
            return
                        
        # search for first index which can swap to increase first_swappable_index
        # we only need to look for first since the increasing condition means
        # all values to the left of that value are increasing

        # since finding first_swappable_index required a previous value that was
        # greater than it, this loop is guaranteed to end
        swap_index = len(nums) - 1
        while nums[swap_index] <= nums[first_swappable_index]:
            swap_index -= 1

        # swap the two indices
        tmp = nums[first_swappable_index]
        nums[first_swappable_index] = nums[swap_index]
        nums[swap_index] = tmp

        # sort everything to the right of the index
        nums[first_swappable_index + 1:] = sorted(nums[first_swappable_index + 1:])


if __name__ == "__main__":
    # nums = [9,3,5,4]
    # Solution().nextPermutation(nums)
    # assert nums == [9,4,3,5]

    # nums = [1,2,3]
    # Solution().nextPermutation(nums)
    # assert nums == [1,3,2]

    # nums = [3,2,1]
    # Solution().nextPermutation(nums)
    # assert nums == [1,2,3]

    # nums = [3,2,1]
    # Solution().nextPermutation(nums)
    # assert nums == [1,2,3]

    # nums = [2,3,1]
    # Solution().nextPermutation(nums)
    # assert nums == [3,1,2]

    nums = [1,5,1]
    Solution().nextPermutation(nums)
    assert nums == [5,1,1]
