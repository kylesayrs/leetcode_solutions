from typing import List, Set, Tuple

from collections import deque


class Solution:
    def dfs(self, i: int, j: int, history: Set[Tuple[int, int]]):
        # boundary condition
        if (
            i < 0 or i >= self.height or
            j < 0 or j >= self.width
        ):
            return False

        # history condition
        if (i, j) in history:
            return False

        # value condition
        if self.board[i][j] != self.word[len(history)]:
            return False
        
        # append to set
        history.add((i, j))
        
        # success condition
        if len(self.word) == len(history):
            return True

        # recursive success
        success = (
            self.dfs(i - 1, j, history) or
            self.dfs(i + 1, j, history) or
            self.dfs(i, j - 1, history) or
            self.dfs(i, j + 1, history)
        )

        # remember to backtrack history
        if success:
            return True
        else:
            history.remove((i, j))
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.width = len(board[0])
        self.height = len(board)
        self.word = word

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, set()):
                    return True
                
        return False


if __name__ == "__main__":
    """
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    assert Solution().exist(board, word) == True

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    assert Solution().exist(board, word) == True

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    assert Solution().exist(board, word) == False
    """
    
    board = [["A","B"],["D","C"]]
    word = "ADC"
    assert Solution().exist(board, word) == True
