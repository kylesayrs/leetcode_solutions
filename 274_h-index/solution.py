from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        0, 1, 3, 5, 6
        """
        citations.sort()

        for h in reversed(range(1, len(citations) + 1)):
            if (citations[len(citations) - h] >= h):
                return h

        return 0
