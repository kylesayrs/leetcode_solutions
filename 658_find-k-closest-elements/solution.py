from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while right - left + 1 > k:
            distance_left = abs(arr[left] - x)
            distance_right = abs(arr[right] - x)

            # lesser numbers are closer, prefer to move right pointer
            if distance_right >= distance_left:
                right -= 1

            else:
                left += 1
    
        return arr[left: right + 1]
    

if __name__ == "__main__":
    assert Solution().findClosestElements([1,2,3,4,5], 4, 3) == [1,2,3,4]
    assert Solution().findClosestElements([1,2,3,4,5], 4, -1) == [1,2,3,4]
    assert Solution().findClosestElements([1,2,3,4,5], 4, 100) == [2,3,4,5]
    assert Solution().findClosestElements([1,2,3,4,5], 4, 1) == [1,2,3,4]
