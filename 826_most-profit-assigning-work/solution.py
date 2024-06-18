from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        O(nlogn + mlogm + n + m)

        jobs sorted by difficulty
        workers sorted by ability

        prev_max_profit = 0
        prev_max_difficulty_index = 0
        max_profit = []
        for i in workers
            max_difficulty_index = prev_max_difficulty_index
            while (difficulty[prev_max_difficulty_index] <= worker[i]):
                max_difficulty_index += 1

            max_profit[i] = max(max_profit[i - 1], profit[prev_max_difficulty_index: max_difficulty_index])

            prev_max_profit = max_profit
            prev_max_difficulty_index = max_difficulty_index

        max_profit[i]
        """

        difficulty, profit = zip(*sorted(zip(difficulty, profit), key=lambda e: e[0]))
        worker.sort()

        max_profit = [0 for _ in range(len(worker))]
        prev_difficulty_index = 0
        for worker_index in range(len(worker)):
            difficulty_index = prev_difficulty_index
            while (
                difficulty_index < len(difficulty) and
                difficulty[difficulty_index] <= worker[worker_index]
            ):
                difficulty_index += 1

            max_profit[worker_index] = max(
                0,
                max_profit[worker_index - 1] if worker_index > 0 else 0,
                *profit[prev_difficulty_index: difficulty_index]
            )

            prev_difficulty_index = difficulty_index

        return sum(max_profit)


if __name__ == "__main__":
    Solution().maxProfitAssignment([13,37,58], [4,90,96], [34,73,45])
