from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        len_nums = len(nums)

        index = 0
        end_index = len(nums) - 1  # last element in natural numbers subarray
        while index < end_index + 1:
            #print((nums, index))
            target_index = nums[index] - 1

            # store negative and large numbers at end of array
            if target_index < 0 or target_index >= len_nums:
                nums[end_index], nums[index] = nums[index], nums[end_index]
                end_index -= 1
                continue

            if target_index != index:
                # store duplicates at end of array
                if nums[target_index] == nums[index]:
                    nums[end_index], nums[index] = nums[index], nums[end_index]
                    end_index -= 1
                    continue

                # swap into correct spot
                nums[target_index], nums[index] = nums[index], nums[target_index]
                continue

            # nums[index] - 1== index
            index += 1

        # after sorting, iterate to find the first missing positive
        first_missing_positive = 1
        for num in nums:
            if num != first_missing_positive:
                break

            else:
                first_missing_positive += 1

        return first_missing_positive
    

if __name__ == "__main__":
    Solution().firstMissingPositive([1, 2, 0])
    Solution().firstMissingPositive([2, 0, 1])
    Solution().firstMissingPositive([1, 0, 2])
    Solution().firstMissingPositive([1, 0, 2, 3])
    Solution().firstMissingPositive([1, 0, 20])
    Solution().firstMissingPositive([1, 1])
            
        
