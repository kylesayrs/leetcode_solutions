from typing import List

from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        freq = defaultdict(lambda: 0)
        for value in hand:
            freq[value] += 1

        for value in hand:
            if freq[value] <= 0:
                continue

            for index in range(groupSize):
                if freq[value + index] <= 0:
                    return False
                    
                freq[value + index] -= 1

        return True
