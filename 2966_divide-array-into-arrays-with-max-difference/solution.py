from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)

        subarrays = [
            [
                nums[subarray_index * 3],
                nums[subarray_index * 3 + 1],
                nums[subarray_index * 3 + 2],
            ]
            for subarray_index in range(len(nums) // 3)
        ]

        for subarray in subarrays:
            if max(subarray) - min(subarray) > k:
                return []
            
        return subarrays


if __name__ == "__main__":
    Solution().divideArray([1, 1, 1, 2, 2, 2, 3, 5, 4], 1)
