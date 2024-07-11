from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Because xor is a toggling operation and is commutative,
        if xor of the same number is applied twice, then it is equivalent
        to the identity
        """
        result = nums[0]
        for num in nums[1:]:
            result ^= num

        return result
