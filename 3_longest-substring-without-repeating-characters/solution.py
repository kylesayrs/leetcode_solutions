class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        string_length = len(s)
        max_substring_length = 0

        string_characters = set()

        while right < string_length:
            next_character = s[right]

            if next_character in string_characters:
                while True:
                    character_to_remove = s[left]
                    string_characters.remove(character_to_remove)
                    left += 1
                    if character_to_remove == next_character:
                        break
                
            string_characters.add(s[right])
            right += 1

            max_substring_length = max(max_substring_length, right - left)

        return max_substring_length


if __name__ == "__main__":
    #Solution().lengthOfLongestSubstring("a") == 1
    #Solution().lengthOfLongestSubstring("aba") == 2
    Solution().lengthOfLongestSubstring("abcabcbb") == 3
