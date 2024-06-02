from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0             # left tracks current position
        right = nums[0] + 1  # right tracks max position from current position
        num_jumps = 0

        # stop if end has been reached
        while left < len(nums) - 1:
            # need another jump to get to next range
            num_jumps += 1

            # calculate next range from current position
            next_right = max(
                (
                    index + nums[index]
                    for index in range(left + 1, right)  # do not need to check current position
                    if index < len(nums)
                ),
                default=0
            )
            left = right - 1        # left is inclusive
            right = next_right + 1  # right is exclusive

        return num_jumps



if __name__ == "__main__":
    assert Solution().jump([0]) == 0
    assert Solution().jump([1]) == 0
    assert Solution().jump([1, 2, 0, 0]) == 2
    assert Solution().jump([1, 2, 3]) == 2
    assert Solution().jump([1, 0]) == 1
    assert Solution().jump([2,3,1,1,4]) == 2
    assert Solution().jump([1, 1, 1, 1]) == 3
