from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subset(idx, ds, nums, ans, n):
            """
            Assume (through recursion) that this function will be called
            with every possible subset to the left of `idx`

            My job is to, given a subset to the left of `idx`, append all
            subsets to the right of `idx` inclusive
            """

            ans.append(ds.copy())

            for i in range(idx, n):
                # always include my index (even if it's a duplicate)
                # do not include future duplicates
                if i == idx or nums[i] != nums[i - 1]:
                    subset(i + 1, ds.copy() + [nums[i]], nums, ans, n)

        n = len(nums)
        ds = []
        ans = []

        nums.sort()

        subset(0, ds, nums, ans, n)
        print(ans)
        return ans

"""
2 x x x
2 2 x x
2 2 2 x
2 2 2 2
"""

if __name__ == "__main__":
        Solution().subsetsWithDup([1, 2, 2, 2, 3, 4])
