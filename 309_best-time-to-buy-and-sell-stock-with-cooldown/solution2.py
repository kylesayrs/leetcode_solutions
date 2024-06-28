from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dfs(index, has_stock)
            dfs(index + 1, has_stock)
            dfs(index + 1, true) - prices[index] if not has_stock
            dfs(index + 2, false) + prices[index] if has_stock
        """

        has_stock = [0, 0]
        no_stock = [0, 0]

        for index in reversed(range(len(prices))):
            today_has_stock = max(
                has_stock[0],
                no_stock[1] + prices[index]
            )

            today_no_stock = max(
                no_stock[0],
                has_stock[0] - prices[index]
            )

            has_stock[1] = has_stock[0]
            no_stock[1] = no_stock[0]
            has_stock[0] = today_has_stock
            no_stock[0] = today_no_stock

        return no_stock[0]
