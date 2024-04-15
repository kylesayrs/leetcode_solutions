from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            # bias left arbitrarily
            middle = (right - left) // 2 + left
            
            # because we biased left, use the movement that doesn't exclude middle
            # when considering the equals case (or just treat equals separately)
            if target <= nums[middle]:
                right = middle

            else:
                # add one to avoid case where left == middle
                left = middle + 1

        assert left == right
        return left if nums[left] == target else -1


if __name__ == "__main__":
    assert Solution().search([1, 2, 3], 1) == 0
    assert Solution().search([1, 2, 3], 2) == 1
    assert Solution().search([1, 2, 3], 3) == 2
    assert Solution().search([1, 2, 3, 4], 1) == 0
    assert Solution().search([1, 2, 3, 4], 2) == 1
    assert Solution().search([1, 2, 3, 4], 3) == 2
    assert Solution().search([1, 2, 3, 4], 4) == 3
