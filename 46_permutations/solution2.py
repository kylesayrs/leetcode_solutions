from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutations = []
        
        # for each number, place it last and recurse on other nums
        # each subtree is disjoint because none of them have the same numbers
        # ONLY BECAUSE ALL NUMBERS IN NUMS ARE DISTINCT
        for _ in range(len(nums)):
            num = nums.pop(0)  # will place last

            partial_permutations = self.permute(nums)
            for partial_permutation in partial_permutations:
                partial_permutation.append(num)  # place last
                permutations.append(partial_permutation)  # record result

            # replace into nums
            nums.append(num)

        return permutations
            

if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
