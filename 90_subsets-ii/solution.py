from typing import List

from collections import defaultdict


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_freq = defaultdict(lambda: 0)
        for num in nums:
            num_freq[num] += 1

        num_freq = list(num_freq.items())
        subsets = []
        def dfs(subset: List[int], index: int):
            nonlocal num_freq
            nonlocal subsets

            if index >= len(num_freq):
                subsets.append(subset)
                return
            
            num, freq = num_freq[index]
            for freq_index in range(0, freq + 1):  # TODO: double check
                _subset = subset.copy()
                _subset += [num] * freq_index
                dfs(_subset, index + 1)

        dfs([], 0)

        return subsets
    
if __name__ == "__main__":
        Solution().subsetsWithDup([1, 2, 2])
