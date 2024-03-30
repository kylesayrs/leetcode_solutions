from typing import List

import math


class Solution:
    def get_days_needed(self, capacity: int, weights: List[int]) -> int:
        """
        This implementation could be improved
        """
        days_needed = 1  # need at least one day if len(weights) > 0
        capacity_used = 0
        
        weight_index = 0
        while weight_index < len(weights):
            weight = weights[weight_index]

            if weight > capacity:
                return math.inf

            if capacity_used + weight > capacity:
                days_needed += 1
                capacity_used = 0

            else:
                capacity_used += weight
                weight_index += 1

        print(f"get_days_needed({capacity}, {weights}) = {days_needed}")
        return days_needed


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = min(weights)
        right = sum(weights)

        while left < right:
            # bais left since we want the minimum capacity which satisfies the
            # condition
            capacity = (right - left) // 2 + left
            days_needed = self.get_days_needed(capacity, weights)

            if days_needed < days:
                right = capacity

            # since we baised left, left needs to add one to avoid condition
            # L == M
            if days_needed > days:
                left = capacity + 1

            # since we're looking for the minimum value, we continue searching
            # left but reduce our search space on the right
            if days_needed == days:
                right = capacity

        assert left == right
        return left


if __name__ == "__main__":
    assert Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5) == 15
