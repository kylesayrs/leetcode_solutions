from typing import List

import heapq

def max_heapify(array: List[int]):
    new_array = [-element for element in array]
    heapq.heapify(new_array)

    return new_array


def max_heap_pop(array: List[int]) -> int:
    return -heapq.heappop(array)


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = max_heapify(happiness)

        total_happiness = 0
        for num_selections in range(k):
            happiest = max_heap_pop(happiness)
            total_happiness += max(happiest - num_selections, 0)

        return total_happiness
