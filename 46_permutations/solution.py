from typing import List, Union


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def dfs(index: int, permutation: List[Union[int, None]]):
            if None not in permutation:
                permutations.append(permutation)
                return
            
            for permutation_index in range(len(permutation)):
                if permutation[permutation_index] is None:
                    p = permutation.copy()
                    p[permutation_index] = nums[index]
                    dfs(index + 1, p)

        dfs(0, [None for _ in range(len(nums))])
        return permutations
