from typing import List

from enum import Enum
from collections import deque

class CellTypes(Enum):
    EMPTY = 0
    ORANGE = 1
    ROTTEN = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # assert len(grid) > 0
        height = len(grid)
        width = len(grid[0])

        # initialize queues
        queue = deque()
        next_queue = deque()

        # ingest initial rotten
        for row in range(height):
            for column in range(width):
                if grid[row][column] == CellTypes.ROTTEN.value:
                    grid[row][column] = CellTypes.ORANGE.value  # pretend fresh orange
                    queue.append((row, column))

        # if rottens were found, then the first step doesn't count since we're
        # pretending they're fresh
        num_steps = -1 if len(queue) > 0 else 0
        
        # iterate simulation
        while len(queue) > 0:
            #print(queue)
            #import numpy; print(numpy.array(grid))

            # step simulation
            proccessed_any = False
            while len(queue) > 0:
                row, column = queue.popleft()

                # check out of bounds
                if (row < 0 or row >= height or column < 0 or column >= width):
                    continue

                # check if not fresh orange
                if grid[row][column] != CellTypes.ORANGE.value:
                    continue

                next_queue.append((row - 1, column))
                next_queue.append((row + 1, column))
                next_queue.append((row, column - 1))
                next_queue.append((row, column + 1))

                # mark processed
                grid[row][column] = CellTypes.ROTTEN.value
                proccessed_any = True

            # increase steps
            if proccessed_any:
                num_steps += 1

            # iterate queue
            queue = next_queue
            next_queue = deque()

        # check if oranges remaining
        for row in range(height):
            for column in range(width):
                if grid[row][column] == CellTypes.ORANGE.value:
                    return -1

        return num_steps
    

if __name__ == "__main__":
    assert Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert Solution().orangesRotting([[0,2]]) == 0
    assert Solution().orangesRotting([[0]]) == 0
    assert Solution().orangesRotting([[2,2],[1,1],[0,0],[2,0]]) == 1


            
