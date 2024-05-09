from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_len = len(p)
        window_freq = [0 for _ in range(26)]
        target_freq = [0 for _ in range(26)]
        num_matches = 26
        anagram_indices = []

        def update(char: s, difference: int):
            nonlocal window_freq
            nonlocal target_freq
            nonlocal num_matches

            char_index = ord(char) - ord('a')

            prev_match = window_freq[char_index] == target_freq[char_index]
            window_freq[char_index] += difference
            now_match = window_freq[char_index] == target_freq[char_index]

            if prev_match and not now_match:
                num_matches -= 1

            if not prev_match and now_match:
                num_matches += 1

        # initialize target_freq
        for char in p:
            char_index = ord(char) - ord('a')
            target_freq[char_index] += 1

        # update matches
        for char_index in range(26):
            if target_freq[char_index] != 0:
                num_matches -= 1

        # initialize window
        for char in s[:p_len]:
            update(char, 1)

        # check for first solution
        if num_matches == 26:
            anagram_indices.append(0)

        # slide window and check for solutions
        for remove_index, char in enumerate(s[p_len:]):
            remove_char = s[remove_index]
            update(remove_char, -1)
            update(char, 1)

            if num_matches == 26:
                anagram_indices.append(remove_index + 1)

        return anagram_indices
