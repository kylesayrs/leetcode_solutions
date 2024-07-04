class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for index in range(len(s)):
            # count odd palidromes
            for radius in range(min(index + 1, len(s) - index)):
                if s[index - radius] == s[index + radius]:
                    count += 1
                else:
                    break

            # count even palidromes
            for radius in range(min(index + 1, len(s) - index - 1)):
                if s[index - radius] == s[index + radius + 1]:
                    count += 1
                else:
                    break

        return count
