from typing import List

import math


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        dfs(index)
        max (
            dfs(index + j) + j * max(arr[index: index + j])
            for j in range(k)
        )
        """

        cache = [None for _ in range(len(arr))]
        def helper(index: int):
            nonlocal arr
            nonlocal cache
            nonlocal k

            if index == len(arr):
                return 0

            if index > len(arr):
                return -math.inf

            # note: max across array call could be memoized
            if cache[index] is None:
                cache[index] = max(
                    helper(index + partition_len) + partition_len * max(arr[index: index + partition_len])
                    for partition_len in range(1, k + 1)
                )
            
            return cache[index]

        return helper(0)
