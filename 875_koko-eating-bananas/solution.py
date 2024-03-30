from typing import List

import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        while left < right:
            # we bais left since the problem wants the min `k` which satisfies
            # the condition
            k = math.floor((right - left) / 2) + left
            hours_needed = sum(int(math.ceil(pile / k)) for pile in piles)
            
            if hours_needed < h:
                right = k

            # since we bais left, we add one to left in order to avoid the infinite
            # state L == M
            if hours_needed > h:
                left = k + 1

            # remember that `hours_needed == h` is only a sign of feasibility
            # but there are many values of k which satisfy `hours_needed == h`
            # we want the min value, so just move right and make sure to include k
            if hours_needed == h:
                right = k

        assert left == right
        return left
        

if __name__ == "__main__":
    assert Solution().minEatingSpeed([1, 1, 1], 3) == 1
    assert Solution().minEatingSpeed([1, 3, 2], 3) == 3
    assert Solution().minEatingSpeed([1, 3, 2], 4) == 2

    assert Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
