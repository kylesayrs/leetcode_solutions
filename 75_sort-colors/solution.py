from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_pointer = 0
        two_pointer = len(nums) - 1
        index = 0
        while index <= two_pointer:
            if nums[index] == 0:
                nums[zero_pointer], nums[index] = nums[index], nums[zero_pointer]
                while nums[zero_pointer] == 0:
                    zero_pointer += 1
                    if zero_pointer >= len(nums):
                        return

                while index < zero_pointer:
                    index += 1

            elif nums[index] == 2:
                nums[two_pointer], nums[index] = nums[index], nums[two_pointer]
                while nums[two_pointer] == 2:
                    two_pointer -= 1
                    if two_pointer < 0:
                        return

            else: # if nums[index] == 1:
                index += 1


if __name__ == "__main__":
    # nums = []
    # Solution().sortColors(nums)
    # assert nums == []

    nums = [1, 2, 2, 2, 0, 1, 0, 2, 0, 1, 0, 1, 2, 0, 2, 1, 1, 2, 0]
    Solution().sortColors(nums)
    print(nums)
    assert nums == list(sorted([1, 2, 2, 2, 0, 1, 0, 2, 0, 1, 0, 1, 2, 0, 2, 1, 1, 2, 0]))

    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)
    assert nums == list(sorted([2,0,2,1,1,0]))

    nums = [0,0,0,0,0,0]
    Solution().sortColors(nums)
    print(nums)
    assert nums == list(sorted([0,0,0,0,0,0]))

    nums = [1,1,1,1,1,1]
    Solution().sortColors(nums)
    print(nums)
    assert nums == list(sorted([1,1,1,1,1,1]))

    nums = [2,2,2,2,2,2]
    Solution().sortColors(nums)
    print(nums)
    assert nums == list(sorted([2,2,2,2,2,2]))

    nums = [0,1,0,1,1,1]
    Solution().sortColors(nums)
    print(nums)
    assert nums == list(sorted([0,1,0,1,1,1]))
