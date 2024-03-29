from typing import List


class Solution:
    def dfs(self, coins, target):
        if target in self.target_cache:
            return self.target_cache[target]

        if target == 0:
            return 0

        if target < 0:
            return float("inf")

        num_coins_needed = 1 + min([
            self.dfs(coins, target - coin)
            for coin in coins
        ])
    
        self.target_cache[target] = num_coins_needed
        return num_coins_needed


    def coinChange(self, coins: List[int], amount: int) -> int:
        self.target_cache = {}

        num_coins_needed = self.dfs(coins, amount)
        if num_coins_needed == float("inf"):
            return -1
        else:
            return num_coins_needed
