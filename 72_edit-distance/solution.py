import math


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [
            [None for _ in range(len(word2) + 1)]
            for _ in range(len(word1) + 1)
        ]

        for index1 in range(len(word1) + 1):
            for index2 in range(len(word2) + 1):
                if index1 == 0 and index2 == 0:
                    cache[index1][index2] = 0
                    continue

                add_cost = (
                    1 + cache[index1 - 1][index2]
                    if index1 - 1 >= 0
                    else math.inf
                )

                remove_cost = (
                    1 + cache[index1][index2 - 1]
                    if index2 - 1 >= 0
                    else math.inf
                )

                replace_cost = (
                    (
                        1 + cache[index1 - 1][index2 - 1]
                        if word1[index1 - 1] != word2[index2 - 1]
                        else 0 + cache[index1 - 1][index2 - 1]
                    )
                    if index1 - 1 >= 0 and index2 - 1 >= 0
                    else math.inf
                )

                cache[index1][index2] = min(
                    add_cost, remove_cost, replace_cost
                )

        return cache[-1][-1]
