class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        palindrome_length = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                palindrome_length += 2

            else:
                seen.add(c)

        if len(seen) > 0:
            palindrome_length += 1

        return palindrome_length
