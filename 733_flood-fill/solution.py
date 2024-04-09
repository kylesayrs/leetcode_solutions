from typing import List

from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])

        queue = deque()
        queue.append((sr, sc))
        start_color = image[sr][sc]
        while len(queue) > 0:
            row, column = queue.pop()

            # oob condition
            if (
                row < 0 or row >= height or
                column < 0 or column >= width
            ):
                continue

            # seen condition
            if image[row][column] == color:
                continue

            # recursive clause
            if image[row][column] == start_color:
                image[row][column] = color
                queue.append((row - 1, column))
                queue.append((row + 1, column))
                queue.append((row, column - 1))
                queue.append((row, column + 1))

        return image
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        start_color = image[sr][sc]

        def dfs(row: int, column: int):
            # oob condition
            if (
                row < 0 or row >= height or
                column < 0 or column >= width
            ):
                return

            # seen condition
            if image[row][column] == color:
                return
            
            # recursive clause
            if image[row][column] == start_color:
                image[row][column] = color
                dfs(row - 1, column)
                dfs(row + 1, column)
                dfs(row, column - 1)
                dfs(row, column + 1)

        dfs(sr, sc)
        return image


if __name__ == "__main__":
    assert Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    assert Solution().floodFill([[0,0,0],[0,0,0]], 0, 0, 0) == [[0,0,0],[0,0,0]]
