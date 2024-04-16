from typing import List


class Solution:
    def dfs(self, string: str, left: int, right: int):
        num_left_in_string = right - left  #(n - left) - (n - right)

        if left > 0:
            self.dfs(f"{string}(", left - 1, right)
        
        if num_left_in_string > 0:
            self.dfs(f"{string})", left, right - 1)

        if left == 0 and num_left_in_string == 0:
            self.result.add(string)


    def generateParenthesis(self, n: int) -> List[str]:
        self.result = set()
        self.dfs("", n, n)

        return self.result


if __name__ == "__main__":
    assert Solution().generateParenthesis(3) == set(["((()))","(()())","(())()","()(())","()()()"])
    assert Solution().generateParenthesis(1) == set(["()"])
    assert Solution().generateParenthesis(4) == set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
