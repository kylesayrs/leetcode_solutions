from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        parities = []
        parity = [False for _ in range(26)]
        zero = ord('a')
        parities.append(parity.copy())
        for char in s:
            parity[ord(char) - zero] = not parity[ord(char) - zero]
            parities.append(parity.copy())

        result = [False for _ in range(len(queries))]
        for q_index, (left, right, k) in enumerate(queries):
            right_parity = parities[right + 1]
            left_parity = parities[left]
            parity = [
                right_parity[index] ^ left_parity[index]
                for index in range(26)
            ]
            result[q_index] = sum(parity) // 2 <= k

        return result
