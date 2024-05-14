from typing import List, Set, Tuple


class Solution:
    def backtrack_max_gold(self, row: int, col: int, seen: Set[Tuple[int, int]]) -> int:
        # out of bounds
        if (
            row < 0 or row >= self.height or
            col < 0 or col >= self.width
        ):
            return 0

        # no gold, cannot recurse
        if self.grid[row][col] == 0:
            return 0
        
        # seen condition
        if (row, col) in seen:
            return 0

        # recurse
        seen.add((row, col))
        max_gold = self.grid[row][col]
        max_gold += max(
            self.backtrack_max_gold(row + 1, col, seen),
            self.backtrack_max_gold(row - 1, col, seen),
            self.backtrack_max_gold(row, col + 1, seen),
            self.backtrack_max_gold(row, col - 1, seen)
        )
        seen.remove((row, col))

        return max_gold


    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid

        max_gold = 0
        for start_row in range(self.height):
            for start_col in range(self.width):
                max_gold = max(
                    max_gold,
                    self.backtrack_max_gold(start_row, start_col, set())
                )

        return max_gold


if __name__ == "__main__":
    assert Solution().getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]) == 24
    assert Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]) == 28
