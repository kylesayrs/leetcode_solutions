from typing import List, Set, Tuple

import math
import numpy


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])

        update_matrix = [[None for _ in range(width)] for _ in range(height)]

        def update_distance_from_zero(row_index: int, column_index: int, seen: Set[Tuple[int, int]]) -> int:
            # oob condition
            if (
                row_index < 0 or row_index >= height or
                column_index < 0 or column_index >= width
            ):
                return math.inf
            
            print(f"    ({row_index} {column_index})")
            
            # success condition
            if mat[row_index][column_index] == 0:
                update_matrix[row_index][column_index] = 0
                return 0
            
            # seen condition
            if update_matrix[row_index][column_index] is not None:
                return update_matrix[row_index][column_index]
            update_matrix[row_index][column_index] = math.inf
            
            # recursive case
            if row_index == 2 and column_index == 2:
                print(numpy.array(update_matrix))

            update_matrix[row_index][column_index] = min(
                update_distance_from_zero(row_index - 1, column_index, seen) + 1,
                update_distance_from_zero(row_index + 1, column_index, seen) + 1,
                update_distance_from_zero(row_index, column_index - 1, seen) + 1,
                update_distance_from_zero(row_index, column_index + 1, seen) + 1,
            )

            return update_matrix[row_index][column_index]

        print(numpy.array(mat))
        for row_index in range(height):
            for column_index in range(width):
                print((row_index, column_index))
                update_distance_from_zero(row_index, column_index, set())

        print(numpy.array(update_matrix))

        return update_matrix
    

if __name__ == "__main__":
    #assert Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
    #assert Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]
    #assert Solution().updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]) == [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
    assert Solution().updateMatrix([[1,0,0],[1,1,1],[1,1,1]]) == [[1,0,0],[2,1,1],[3,2,2]]
                
