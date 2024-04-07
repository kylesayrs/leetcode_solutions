class Solution:
    def helper(self, index: int, num_left: int):
        if self.cache[index][num_left] is not None:
            return self.cache[index][num_left]

        if num_left < 0:
            self.cache[index][num_left] = False

        elif index >= len(self.string):
            if num_left > 0:
                self.cache[index][num_left] = False
            else:
                self.cache[index][num_left] = True

        elif self.string[index] == "(":
            self.cache[index][num_left] = self.helper(index + 1, num_left + 1)

        elif self.string[index] == ")":
            self.cache[index][num_left] = self.helper(index + 1, num_left - 1)

        else: # self.string[0] == "*":
            self.cache[index][num_left] = (
                self.helper(index + 1, num_left - 1) or
                self.helper(index + 1, num_left + 1) or
                self.helper(index + 1, num_left)
            )
        
        return self.cache[index][num_left]


    def checkValidString(self, s: str) -> bool:
        self.string = s
        self.cache = [[None for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        return self.helper(0, 0)



if __name__ == "__main__":
    assert Solution().checkValidString("") == True
    assert Solution().checkValidString("()") == True
    assert Solution().checkValidString("(*)") == True
    assert Solution().checkValidString("(*))") == True
    assert Solution().checkValidString("(*)))") == False
    assert Solution().checkValidString("(*))(") == False
