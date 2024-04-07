class Solution:
    def maxDepth(self, s: str) -> int:
        left_len = 0
        max_left_len = 0
        
        for char in s:
            if char == "(":
                left_len += 1
                max_left_len = max(max_left_len, left_len)

            if char == ")":
                left_len -= 1

        return max_left_len


if __name__ == "__main__":
    assert Solution().maxDepth("") == 0
    assert Solution().maxDepth("()") == 1
    assert Solution().maxDepth("()()") == 1
    assert Solution().maxDepth("()(()())") == 2
