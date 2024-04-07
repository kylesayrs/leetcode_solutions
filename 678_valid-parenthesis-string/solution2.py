class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0
        for char in s:
            if char == "(":
                left_min += 1
                left_max += 1

            elif char == ")":
                if left_max <= 0:
                    return False
                
                left_min -= 1
                left_max -= 1

            else:  # char == "*"
                left_min -= 1
                left_max += 1

            left_min = max(left_min, 0)

        return left_min == 0
                

if __name__ == "__main__":
    assert Solution().checkValidString("") == True
    assert Solution().checkValidString("()") == True
    assert Solution().checkValidString("(*)") == True
    assert Solution().checkValidString("(*))") == True
    assert Solution().checkValidString("(*)))") == False
    assert Solution().checkValidString("(*))(") == False
