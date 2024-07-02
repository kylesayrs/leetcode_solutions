from typing import List

import math


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # assert len(customers) == len(grumpy)

        current_value = 0
        max_value = -math.inf
        for right in range(len(customers)):
            # update right
            if grumpy[right]:
                current_value += customers[right]

            # store value
            max_value = max(max_value, current_value)

            # full window
            if right + 1 >= minutes:
                # could also store max here if only applies to full windows

                # set up for next iteration
                left = right - minutes + 1
                if grumpy[left]:
                    current_value -= customers[left]

        total_satisfied = sum([
            customers[index]
            for index in range(len(customers))
            if not grumpy[index]
        ]) + max_value

        return total_satisfied
