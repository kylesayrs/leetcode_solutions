from typing import List


class Solution:
    def positions_to_image(positions: List[int]) -> List[str]:
        n = len(positions)

        image = [
            "".join(["Q" if col == position else "." for col in range(n)])
            for position in positions
        ]
        
        return image


    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []    

        def dfs(positions: List[int]):
            #print(f"dfs positions: {positions}")
            row_index = len(positions)

            if row_index >= n:
                solutions.append(positions[:])  # deep copy
                return

            for column_index in range(n):
                for prev_row, prev_col in enumerate(positions):
                    # check columns
                    if column_index == prev_col:
                        break
                    
                    # check negative diagonals
                    neg_offset = column_index - row_index
                    prev_neg_offset = prev_col - prev_row
                    if neg_offset == prev_neg_offset:
                        break

                    # check negative diagonals
                    pos_offset = (n - column_index) - row_index
                    prev_pos_offset = (n - prev_col) - prev_row
                    if pos_offset == prev_pos_offset:
                        break

                # recurse on valid moves
                else:
                    positions.append(column_index)
                    dfs(positions)
                    positions.pop()

        dfs([])
        
        # convert solutions to proper format
        return [
            Solution.positions_to_image(positions) for positions in solutions
        ]


if __name__ == "__main__":
    print(Solution().solveNQueens(4))
