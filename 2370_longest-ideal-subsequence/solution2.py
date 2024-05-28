class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        cache = [0 for _ in range(26)]
        for index in range(len(s)):
            cache_index = ord(s[index]) - ord('a')

            cache[cache_index] = max(
                cache[max(cache_index - k, 0): min(cache_index + k + 1, 26)]
            ) + 1

        return max(cache)


if __name__ == "__main__":
    Solution().longestIdealString("azazaz", 25)
