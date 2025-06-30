from collections import defaultdict class Solution:
    def findLHS(self, nums):
        counts = defaultdict(lambda: 0) for num in nums:
            counts[num] += 1
        return max(
            (
                counts[num] + counts[num + 1] for num in nums if (num + 1)
                in counts
            ), default=0
        )
