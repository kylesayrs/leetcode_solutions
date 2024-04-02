from typing import List

import sys


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda pair: pair[1])

        max_len = 0
        prev_end = -sys.maxsize - 1
        for pair in pairs:
            if prev_end < pair[0]:
                max_len += 1
                prev_end = pair[1]

        return max_len
