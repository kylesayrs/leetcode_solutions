import math

class Solution:
    def numWays(self, s: str) -> int:
        """
            x = count num of ones O(n)
            if x not divisible by 3, return false

            if x == 0, return (n - 1) choose 2

            move left1 until reached x/3,
            move left2 until reached first 1
            move right1 until counted another x/3
            move right2 until reached first 1

            return (left2 - left1 + 1) * (right2 - right1 + 1)
        """
        ones_positions = [
            index
            for index, char in enumerate(s)
            if char == '1'
        ]

        if len(ones_positions) == 0:
            return math.comb(len(s) - 1, 2) % (10 ** 9 + 7)

        if len(ones_positions) % 3 != 0:
            return 0

        split_len = len(ones_positions) // 3
        return (
            (ones_positions[split_len] - ones_positions[split_len - 1]) *
            (ones_positions[split_len * 2] - ones_positions[split_len * 2 - 1])
        ) % (10 ** 9 + 7)
