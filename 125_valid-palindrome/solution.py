class Solution:
    def isAlphaNumeric(char: str):
        char_ord = ord(char)

        is_alpha = char_ord >= ord("a") and char_ord <= ord("z")
        is_numeric = char_ord >= ord("0") and char_ord <= ord("9")

        return is_alpha or is_numeric
        

    def isPalindrome(self, s: str) -> bool:
        string = list(filter(Solution.isAlphaNumeric, list(s.lower())))

        left = 0
        right = len(string) - 1
        
        while left < right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1

        return True
            
