import math
import numpy
from collections import defaultdict


class Solution:
    """
    def numSquares(self, n: int) -> int:
        max_square_root = math.ceil(math.sqrt(n))
        cache = defaultdict(lambda: math.inf)

        for root_index in range(max_square_root + 1):
            cache[(0, root_index)] = 0

        for root_index in range(max_square_root + 1):
            root_squared = (root_index + 1) ** 2

            for score in range(1, n + 1):
                cache[(score, root_index)] = min(
                    cache[(score, root_index - 1)],                # do not include
                    cache[(score - root_squared, root_index)] + 1  # include
                )

        return cache[(n, max_square_root)]
    """
    #"""
    def numSquares(self, n: int) -> int:
        max_square_root = math.ceil(math.sqrt(n))
        cache = [[math.inf for _ in range(max_square_root + 1)] for _ in range(n + 1)]

        for root_index in range(max_square_root + 1):
            cache[0][root_index] = 0

        for root_index in range(max_square_root + 1):
            root_squared = (root_index + 1) * 2

            for score in range(1, n + 1):
                not_include_score = (
                    cache[score][root_index - 1]
                    if root_index > 0
                    else math.inf
                )

                include_score = (
                    cache[score - root_squared][root_index] + 1
                    if score - root_squared >= 0
                    else math.inf
                )

                cache[score][root_index] = min(not_include_score, include_score)

        return cache[n][max_square_root]
        #"""

if __name__ == "__main__":
    assert Solution().numSquares(12) == 3
