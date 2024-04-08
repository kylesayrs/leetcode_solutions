from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[None for _ in range(len(text2))] for _ in range(len(text1))]

        for index1 in range(len(text1)):
            for index2 in range(len(text2)):
                if text1[index1] == text2[index2]:
                    cache[index1][index2] = (
                        cache[index1 - 1][index2 - 1] + 1
                        if index1 - 1 >= 0 and index2 - 1 >= 0
                        else 1
                    )

                else:
                    prev1_length = (
                        cache[index1 - 1][index2]
                        if index1 - 1 >= 0
                        else 0
                    )

                    prev2_length = (
                        cache[index1][index2 - 1]
                        if index2 - 1 >= 0
                        else 0
                    )

                    cache[index1][index2] = max(prev1_length, prev2_length)

        return cache[len(text1) - 1][len(text2) - 1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = defaultdict(lambda: 0)

        for index1 in range(len(text1)):
            for index2 in range(len(text2)):
                if text1[index1] == text2[index2]:
                    cache[index1, index2] = cache[index1 - 1, index2 - 1] + 1

                else:
                    cache[index1, index2] = max(cache[index1 - 1, index2], cache[index1, index2 - 1])

        return cache[len(text1) - 1, len(text2) - 1]
    
    
if __name__ == "__main__":
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3
    assert Solution().longestCommonSubsequence("abc", "abc") == 3
    assert Solution().longestCommonSubsequence("abc", "def") == 0
    assert Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1
    assert Solution().longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy") == 2
    assert Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd") == 4
