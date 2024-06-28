from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        def dfs(index: int, subset: List[int]):
            nonlocal subsets

            if index >= len(nums):
                subsets.append(subset.copy())
                return

            # include
            subset.append(nums[index])
            dfs(index + 1, subset)
            subset.pop()

            # do not include
            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            dfs(index + 1, subset)

        dfs(0, [])
        return subsets
