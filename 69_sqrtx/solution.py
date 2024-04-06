import math


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left < right:
            # bias right since we're looking for a min
            middle = math.ceil((right - left) / 2) + left

            middle_squared = middle * middle
            if middle_squared > x:
                right = middle - 1  # avoid infinite case right == middle

            elif middle_squared < x:
                left = middle

            else:
                return middle
            
        assert left == right
        return left


if __name__ == "__main__":
    #assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
