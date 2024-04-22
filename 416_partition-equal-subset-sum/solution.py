from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        
        target = nums_sum // 2

        cache = [False for _ in range(target + 1)]
        cache[0] = True

        for num in nums:
            new_cache = [
                (
                    (index - num >= 0 and cache[index - num]) or
                    cache[index]
                )
                for index in range(target + 1)
            ]

            if new_cache[target] == True:
                return True

            cache = new_cache

        return False


if __name__ == "__main__":
    assert Solution().canPartition([1, 3, 4, 2]) == True
