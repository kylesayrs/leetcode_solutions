from typing import Dict

from collections import defaultdict


class Solution:
    def substring_includes_target(substring_freq: Dict[str, int], target_freq: Dict[str, int]) -> bool:
        for char in target_freq:
            if substring_freq[char] < target_freq[char]:
                return False
            
        return True
    

    def minWindow(self, s: str, t: str) -> str:
        if len(t) <= 0:
            return ""

        # construct frequency dictionaries
        substring_freq = defaultdict(lambda: 0)
        target_freq = defaultdict(lambda: 0)
        for char in t:
            target_freq[char] += 1

        # cache optimal substring
        min_substring = None

        # left pointer right pointer
        left = 0
        for right in range(len(s)):
            substring_freq[s[right]] += 1
            
            while (
                substring_freq[s[left]] > target_freq[s[left]] and
                left < right
            ):
                substring_freq[s[left]] -= 1
                left += 1

            # update min substring if matching target
            if Solution.substring_includes_target(substring_freq, target_freq):
                if min_substring is None or (right - left + 1) < len(min_substring):
                    min_substring = s[left: right + 1]

        return min_substring if min_substring is not None else ""


if __name__ == "__main__":
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"

    assert Solution().minWindow("A", "") == ""
    assert Solution().minWindow("A", "A") == "A"
    assert Solution().minWindow("A", "AA") == ""

    assert Solution().minWindow("BAAAAAAAAAAABC", "ABC") == "ABC"
