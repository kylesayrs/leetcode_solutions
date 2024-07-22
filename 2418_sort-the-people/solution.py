from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_names = zip(heights, names)
        heights_names_sorted = sorted(heights_names, key=lambda e: e[0], reverse=True)
        names_sorted = list(zip(*heights_names_sorted))[1]
        return names_sorted
