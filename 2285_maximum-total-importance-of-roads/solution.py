from typing import List

from collections import defaultdict


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = defaultdict(lambda: 0)
        for road in roads:
            degrees[road[0]] += 1
            degrees[road[1]] += 1

        degrees = sorted([degree for node, degree in degrees.items()], reverse=True)

        _sum = 0
        values = reversed(range(1, n + 1))
        for index, value in enumerate(values):
            if index < len(degrees):
                _sum += degrees[index] * value

        return _sum
