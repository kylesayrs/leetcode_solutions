from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        #print(nums)
        
        while left < right:
            # arbitrarily bias left
            middle = (right - left) // 2 + left

            # find where min is
            min_on_left = nums[middle] < nums[left]    # min in (L, M]
            min_on_right = nums[right] < nums[middle]  # min in (M, R]

            # L[ A ]m[ B ]M( C ]R
            if min_on_left:
                # target in B
                if target <= nums[middle]:
                    right = middle

                # target in C
                elif target <= nums[right]:
                    left = middle + 1

                # target in A
                else:
                    right = middle

            # L[ A )M( B ]m[ C ]R
            elif min_on_right:
                # target in B
                if target > nums[middle]:
                    left = middle + 1

                # target in C
                elif target <= nums[right]:
                    left = middle + 1

                # target in A
                else:
                    right = middle
                    
            # min not in (L, M]U(M, R] => min == L
            # L[ A ]M( B ]R
            else:
                # target in A
                if target <= nums[middle]:
                    right = middle

                # target in B
                else:
                    left = middle + 1

        assert left == right
        return left if nums[left] == target else -1
    

    def search_optimized(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            # arbitrarily bias left
            middle = (right - left) // 2 + left

            # L[ A ]m[ B ]M( C ]R
            if nums[middle] < nums[left]:
                # target in B or A
                if target <= nums[middle] or target > nums[right]:
                    right = middle

                # target in C
                else:
                    left = middle + 1

            # L[ A )M( B ]m[ C ]R
            elif nums[right] < nums[middle]:
                # target in B or C
                if target > nums[middle] or target <= nums[right]:
                    left = middle + 1

                # target in A
                else:
                    right = middle
                    
            # min not in (L, M]U(M, R] => min == L
            # L[ A ]M( B ]R
            else:
                # target in A
                if target <= nums[middle]:
                    right = middle

                # target in B
                else:
                    left = middle + 1

        return left if nums[left] == target else -1
                
if __name__ == "__main__":
    assert Solution().search([1, 2, 3, 4], 2) == 1

    assert Solution().search([4, 1, 2, 3], 1) == 1
    assert Solution().search([4, 1, 2, 3], 2) == 2
    assert Solution().search([4, 1, 2, 3], 3) == 3
    assert Solution().search([4, 1, 2, 3], 4) == 0

    assert Solution().search([4,5,6,7,0,1,2], 0) == 4
    assert Solution().search([4,5,6,7,0,1,2], 3) == -1
    assert Solution().search([1], 0) == -1
