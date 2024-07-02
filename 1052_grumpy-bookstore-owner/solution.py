from typing import List

import math


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # assert len(customers) == len(grumpy)

        current_value = 0
        max_value = -math.inf  # change if customers[i] < 0
        for right in range(len(customers)):
            if grumpy[right]:
                current_value += customers[right]

            max_value = max(max_value, current_value)

            if right + 1 >= minutes:
                # could also store max here if only applies to full windows

                left = right - minutes + 1
                # set up for next iteration
                if grumpy[left]:
                    current_value -= customers[left]

        total_satisfied = sum([
            customers[index]
            for index in range(len(customers))
            if not grumpy[index]
        ]) + max_value

        return total_satisfied
