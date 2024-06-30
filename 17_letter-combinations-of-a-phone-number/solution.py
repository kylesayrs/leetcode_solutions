from typing import List


class Solution:
    digit_to_letters = [
        [],
        [],
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
        ["j", "k", "l"],
        ["m", "n", "o"],
        ["p", "q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"]
    ]
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        def dfs(index: int, comb: str):
            nonlocal combinations

            if index >= len(digits):
                if comb != "":
                    combinations.append(comb)
                return

            for letter in Solution.digit_to_letters[int(digits[index])]:
                dfs(index + 1, comb + letter)
                
        dfs(0, "")

        return combinations
