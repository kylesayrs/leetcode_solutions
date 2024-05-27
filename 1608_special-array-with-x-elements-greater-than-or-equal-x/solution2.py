# counting sort
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # counting sort
        freq = [0 for _ in range(len(nums))]
        num_greq = 0
        for num in nums:
            # assert num >= 0
            if num >= len(nums):
                num_greq += 1
            else:
                freq[num] += 1

        # linear search (binary search requires a linear preprocessing step)
        for i in reversed(range(len(nums) + 1)):
            if i < len(nums):
                num_greq += freq[i]

            if num_greq == i:
                return i
            
        return -1


if __name__ == "__main__":
    #assert Solution().specialArray([3, 5]) == 2
    assert Solution().specialArray([0,4,3,0,4]) == 3
