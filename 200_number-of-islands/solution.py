from typing import List

from enum import StrEnum

class Tile(StrEnum):
    WATER = "0"
    ISLAND = "1"
    MARKED = "2"


class Solution:
    def mark_island(self, row: int, column: int):
        if (
            row < 0 or row >= self.height or
            column < 0 or column >= self.width
        ):
            return
        
        if self.grid[row][column] != Tile.ISLAND:
            return

        self.grid[row][column] = Tile.MARKED
        self.mark_island(row - 1, column)
        self.mark_island(row + 1, column)
        self.mark_island(row, column - 1)
        self.mark_island(row, column + 1)


    def numIslands(self, grid: List[List[str]]) -> int:
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid

        num_islands = 0
        for row in range(self.height):
            for column in range(self.width):                
                if self.grid[row][column] == Tile.WATER or self.grid[row][column] == Tile.MARKED:
                    continue

                num_islands += 1
                self.mark_island(row, column)
        
        return num_islands
