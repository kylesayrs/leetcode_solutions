from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for value in arr:
            if value * 2 in seen or value / 2 in seen:
                return True
            
            seen.add(value)

        return False
