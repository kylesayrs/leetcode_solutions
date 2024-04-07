from typing import List, Set


class Solution:
    def dfs(self, coins_discarded: int, amount_left: int) -> int:
        if amount_left == 0:
            return 1
        
        if amount_left < 0:
            return 0
        
        if coins_discarded >= len(self.coins):
            return 0
        
        if self.cache[amount_left][coins_discarded] is None:
            self.cache[amount_left][coins_discarded] = (
                self.dfs(coins_discarded, amount_left - self.coins[coins_discarded]) +
                self.dfs(coins_discarded + 1, amount_left)
            )
        
        return self.cache[amount_left][coins_discarded]


    def change(self, amount: int, coins: List[int]) -> int:
        self.coins = coins
        self.cache = [[None for _ in range(len(coins))] for _ in range(amount + 1)]
        
        return self.dfs(0, amount)


if __name__ == "__main__":
    assert Solution().change(0, [1, 2, 3]) == 1
    assert Solution().change(3, [2]) == 0
    assert Solution().change(5, [1, 2, 5]) == 4
