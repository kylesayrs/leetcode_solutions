from typing import List, Tuple

import numpy


class Solution:
    def longest_common_substring(self, s1: str, s2: str) -> str:
        cache: List[List[int]] = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

        max_start = [0, 0]
        max_len = 0
        for index1 in reversed(range(len(s1))):
            for index2 in reversed(range(len(s2))):
                if s1[index1] == s2[index2]:
                    cache[index1][index2] = (
                        cache[index1 + 1][index2 + 1]
                        if index1 + 1 < len(s1) and index2 + 1 < len(s2)
                        else 0
                    ) + 1

                    if cache[index1][index2] > max_len:
                        max_len = cache[index1][index2]
                        max_start = [index1, index2]

        assert s1[max_start[0]: max_start[0] + max_len] == s2[max_start[1]: max_start[1] + max_len]
        return s1[max_start[0]: max_start[0] + max_len]


if __name__ == "__main__":
    assert Solution().longest_common_substring("asdf", "asdf") == "asdf"
    assert Solution().longest_common_substring("asdfjjjjj", "asdf") == "asdf"
    assert Solution().longest_common_substring("asdfjjjjj", "asdf;lkj") == "asdf"
    assert Solution().longest_common_substring("adfjjjjjasdf", "asdf;lkj") == "asdf"
