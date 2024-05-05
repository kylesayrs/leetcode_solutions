from typing import List

import numpy


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            num_zeros = s.count("0")
            num_ones = len(s) - num_zeros

            # print("cache")
            # print(numpy.array(cache))

            include_cache = [
                [
                    cache[m_index + num_zeros][n_index + num_ones] + 1
                    if m_index + num_zeros < m + 1 and n_index + num_ones < n + 1
                    else 0
                    for n_index in range(n + 1)
                ]
                for m_index in range(m + 1)
            ]
            # print("include_cache")
            # print(numpy.array(include_cache))
            
            cache = [
                [
                    max(include_cache[m_index][n_index], cache[m_index][n_index])
                    for n_index in range(n + 1)
                ]
                for m_index in range(m + 1)
            ]
            # print("new cache")
            # print(numpy.array(cache))

        return cache[0][0]

if __name__ == "__main__":
    # assert Solution().findMaxForm(["1"], 0, 0) == 0
    # assert Solution().findMaxForm(["1", "1"], 0, 2) == 2
    # assert Solution().findMaxForm(["1", "11"], 0, 2) == 1
    # assert Solution().findMaxForm(["1", "11", "1"], 0, 2) == 2
    assert Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3) == 4
    assert Solution().findMaxForm(["10","0","1"], 1, 1) == 2
