class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        if len(s2) < l:
            return False

        s1_freq = [0 for _ in range(26)]
        s2_freq = [0 for _ in range(26)]

        def update_state(char: str, add: bool):
            nonlocal s1_freq
            nonlocal s2_freq
            nonlocal num_matches

            char_index = ord(char) - ord('a')
            prev_match = s1_freq[char_index] == s2_freq[char_index]
            s2_freq[char_index] += 1 if add else -1
            now_match = s1_freq[char_index] == s2_freq[char_index]

            if not prev_match and now_match:
                num_matches += 1

            if prev_match and not now_match:
                num_matches -= 1

        # initialize s1_freq
        for char in s1:
            char_index = ord(char) - ord('a')
            s1_freq[char_index] += 1

        # initialize num_matches
        num_matches = sum(1 if s1_freq[index] == s2_freq[index] else 0 for index in range(26))

        # initial buildup
        for char in s2[:l]:
            update_state(char, add=True)

        # check for solution
        if num_matches == 26:
            return True

        # match checking
        for left_index, char in enumerate(s2[l:]):
            update_state(s2[left_index], add=False)
            update_state(char, add=True)
            if num_matches == 26:
                return True
            
        return False


if __name__ == "__main__":
    assert Solution().checkInclusion("abc", "abc") == True
    assert Solution().checkInclusion("abc", "ab") == False
    assert Solution().checkInclusion("abc", "abcd") == True
    assert Solution().checkInclusion("abc", "cabd") == True
    assert Solution().checkInclusion("abc", "cabbd") == True
    assert Solution().checkInclusion("abc", "cadbd") == False
    assert Solution().checkInclusion("abc", "cabddddbacd") == True
    assert Solution().checkInclusion("aaa", "caaabddddbacd") == True
    assert Solution().checkInclusion("aaa", "aaabddddbacd") == True
    assert Solution().checkInclusion("ab", "eidbaooo") == True
