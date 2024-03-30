from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            # bias left since we're looking for a min
            middle = (right - left) // 2 + left
            
            # out of order, min must be inbetween
            if nums[left] > nums[middle]:
                right = middle

            # out of order, min must be inbetween
            # since we biased left, we need to add one to left to avoid the
            # infinite condition L == M
            elif nums[right] < nums[middle]:
                left = middle + 1

            # if numbers are ascending between left and right, then search left
            else:
                right = middle

        assert left == right
        return nums[left]
                
        

if __name__ == "__main__":
    assert Solution().findMin([0, 1, 2]) == 0
    assert Solution().findMin([2, 0, 1]) == 0
    assert Solution().findMin([1, 2, 0]) == 0

    assert Solution().findMin([3,4,5,1,2]) == 1
    assert Solution().findMin([4,5,6,7,0,1,2]) == 0
    assert Solution().findMin([11,13,15,17]) == 11
