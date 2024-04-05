class Solution:
    def __init__(self) -> None:
        self.cache = {}
        self.modulus = 10**9 + 7


    def dfs_helper(self, pos_x: int, pos_y: int, moves_left: int) -> int:
        # boundary/ red space condition
        if (
            pos_x < 0 or pos_x >= 3 or
            pos_y < 0 or pos_y >= 4 or
            (pos_x == 0 and pos_y == 3) or
            (pos_x == 2 and pos_y == 3)
        ):
            return 0
        
        # success condition
        if moves_left <= 0:
            return 1
        
        # cache condition
        if (pos_x, pos_y, moves_left) in self.cache:
            return self.cache[(pos_x, pos_y, moves_left)]
        
        # recurse
        num_ways = (
            self.dfs_helper(pos_x - 1, pos_y - 2, moves_left - 1) +
            self.dfs_helper(pos_x - 1, pos_y + 2, moves_left - 1) +
            self.dfs_helper(pos_x + 1, pos_y - 2, moves_left - 1) +
            self.dfs_helper(pos_x + 1, pos_y + 2, moves_left - 1) +

            self.dfs_helper(pos_x - 2, pos_y - 1, moves_left - 1) +
            self.dfs_helper(pos_x - 2, pos_y + 1, moves_left - 1) +
            self.dfs_helper(pos_x + 2, pos_y - 1, moves_left - 1) +
            self.dfs_helper(pos_x + 2, pos_y + 1, moves_left - 1)
        )

        # return and cache
        self.cache[(pos_x, pos_y, moves_left)] = num_ways
        return num_ways % self.modulus


    def knightDialer(self, n: int) -> int:
        return sum([
            self.dfs_helper(pos_x, pos_y, n - 1)
            for pos_x in range(3)
            for pos_y in range(4)
        ]) % self.modulus


if __name__ == "__main__":
    assert Solution().knightDialer(1) == 10
    assert Solution().knightDialer(2) == 20
