from typing import List


class Solution:
    def dfs(self, index: int, combination: List[int]):
        print(f"dfs({index}, {combination})")
        if index >= len(self.candidates):
            return
    
        if sum(combination) > self.target:
            return
        
        if sum(combination) == self.target:
            self.result.append(combination)
            return
        
        self.dfs(index, combination.copy() + [self.candidates[index]])
        self.dfs(index + 1, combination.copy())


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.result = []
        
        self.dfs(0, [])

        return self.result


if __name__ == "__main__":
    assert Solution().combinationSum([2, 1], 5) == [[2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
