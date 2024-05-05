from typing import List

from collections import defaultdict


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = defaultdict(lambda: 0)

        for string_index in range(len(strs)):
            num_zeros = strs[string_index].count('0')
            num_ones = strs[string_index].count('1')

            #for i in range(num_zeros, m + 1):
            #    for j in range(num_ones, n + 1):

            for i in range(num_zeros, m + 1):
                for j in range(num_ones, n + 1):
                    cache[(string_index, i, j)] = max(
                        cache[(string_index - 1, i, j)],  # do not include string
                        cache[(string_index, i - num_zeros, j - num_ones)] + 1,  # include string
                    )

            print((string_index, i, j))

        print(cache)
        print(cache[len(strs) - 1, m, n])
        return cache[len(strs) - 1, m, n]


if __name__ == "__main__":
    assert Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3) == 4
