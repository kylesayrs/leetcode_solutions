from typing import List

from collections import defaultdict


class Solution:
    """
    def num_ways(self, index: int, left: int) -> int:
        if (index, left) in self.cache:
            return self.cache[(index, left)]
        
        # reached end of nums
        if index >= len(self.nums):
            if left == 0:
                return 1
            else:
                return 0
        
        return (
            self.num_ways(index + 1, left - self.nums[index]) +
            self.num_ways(index + 1, left + self.nums[index])
        )

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cache = {}
        self.nums = nums

        return self.num_ways(0, target)
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev_targets = defaultdict(lambda: 0)
        prev_targets[0] = 1
        for i in reversed(range(len(nums))):
            targets = defaultdict(lambda: 0)
            for prev_target, prev_target_num_ways in prev_targets.items():
                targets[prev_target - nums[i]] += prev_target_num_ways
                targets[prev_target + nums[i]] += prev_target_num_ways

            prev_targets = targets

        return prev_targets[target]


if __name__ == "__main__":
    print(Solution().findTargetSumWays([1, 1, 1], 1))
    #print(Solution().findTargetSumWays([1, 1, 1], 2))
