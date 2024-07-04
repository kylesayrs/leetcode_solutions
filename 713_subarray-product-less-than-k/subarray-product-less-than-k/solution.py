from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        total = 1
        total_num_subarrays = 0

        for right in range(len(nums)):
            total *= nums[right]
            
            empty_subarray = False
            while total >= k:
                if left >= right:
                    empty_subarray = True
                    break

                total /= nums[left]
                left += 1

            if empty_subarray:
                continue

            # answers the question how many additional subarrays are created when
            # adding an additional element on the right
            total_num_subarrays += right - left + 1
            
        return total_num_subarrays
        

if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK([1, 2, 3], 0))
    print(Solution().numSubarrayProductLessThanK([1, 2, 3], 2))
    print(Solution().numSubarrayProductLessThanK([2, 1, 3], 2))
    print(Solution().numSubarrayProductLessThanK([3, 2, 1], 2))
