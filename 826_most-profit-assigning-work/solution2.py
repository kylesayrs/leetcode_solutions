from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        # O(n * m)
        # assert len(difficulty) == len(profit) == len(worker)
        max_profit = 0
        """

        for worker_index in range(len(worker)):
            available_profits = []
            for job_index in range(len(difficulty)):
                if difficulty[job_index] <= worker[worker_index]:
                    available_profits.append(profit[job_index])

            max_profit += max(available_profits, default=0)

        return max_profit
