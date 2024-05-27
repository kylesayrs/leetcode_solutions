from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        pointer = len(nums)

        for i in reversed(range(0, len(nums) + 1)):
            while pointer - 1 >= 0 and nums[pointer - 1] >= i:
                pointer -= 1

            print(f"{i}: {pointer}")

            if len(nums) - pointer == i:
                return i
            
        return -1


if __name__ == "__main__":
    #assert Solution().specialArray([3, 5]) == 2
    assert Solution().specialArray([0,4,3,0,4]) == 3
