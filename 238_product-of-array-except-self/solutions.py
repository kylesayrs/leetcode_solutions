from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in range(len(nums))]

        prefix_product = 1
        for index, num in enumerate(nums):
            output[index] *= prefix_product
            prefix_product *= num

        suffix_product = 1
        for index, num in reversed(tuple(enumerate(nums))):
            output[index] *= suffix_product
            suffix_product *= num

        return output
