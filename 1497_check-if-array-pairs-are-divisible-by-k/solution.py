from typing import List

from collections import defaultdict


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_counts = defaultdict(lambda: 0)

        for num in arr:
            remainder_counts[num % k] += 1

        k_is_even = k % 2 == 0
        k_divided_by_two = k // 2
        for remainder in remainder_counts:
            # zero case
            if remainder == 0:
                if remainder_counts[remainder] % 2 != 0:
                    return False

            # half case                
            elif k_is_even and remainder == k_divided_by_two:
                if remainder_counts[remainder] % 2 != 0:
                    return False

            # addend case
            elif remainder_counts[remainder] != remainder_counts[k - remainder]:
                return False
            
        return True


if __name__ == "__main__":
    # assert Solution().canArrange([1,2,3,4,5,10,6,7,8,9], 5) == True
    # assert Solution().canArrange([1,2,3,4,5,6], 7) == True
    # assert Solution().canArrange([1,2,3,4,5,6], 10) == False
    assert Solution().canArrange([2,3,7,-9,4,4,7,3,2,10,8,15,2,1,-8,10,-5,10,-2,21,9,20,0,4,24,5,12,-10,8,9,18,13,-8,10,-4,-3,0,16,-4,8,14,15,-9,0,0,-6,11,-3,10,11,7,-1,-5,5,11,2,5,9,-2,8,9,-10,6,-2,7,8,3,0,-2,11], 18)
