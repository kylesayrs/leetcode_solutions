class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths_starting_at = [
            [-1 for _ in range(n)]
            for _ in range(m)
        ]

        for row in range(m):
            num_paths_starting_at[row][-1] = 1

        for col in range(n):
            num_paths_starting_at[-1][col] = 1

        for row in reversed(range(0, m - 1)):
            for col in reversed(range(0, n - 1)):
                num_paths_starting_at[row][col] = (
                    num_paths_starting_at[row + 1][col] +
                    num_paths_starting_at[row][col + 1]
                )

        return num_paths_starting_at[0][0]
    

    def uniquePaths_optimized(self, m: int, n: int) -> int:
        prev_row = [1 for _ in range(n)]
        for row in reversed(range(0, m - 1)):
            prev_col = 1
            for col in reversed(range(0, n - 1)):
                num_paths = prev_row[col] + prev_col
                prev_row[col] = num_paths
                prev_col = num_paths

        return prev_row[0]


if __name__ == "__main__":
    assert Solution().uniquePaths_optimized(1, 1) == 1
    assert Solution().uniquePaths_optimized(2, 2) == 2
    assert Solution().uniquePaths_optimized(3, 7) == 28
    assert Solution().uniquePaths_optimized(3, 2) == 3
