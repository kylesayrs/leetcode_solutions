from typing import List, Tuple, Any


class DefaultCache:
    def __init__(self, rows: int, columns: int, default: Any) -> None:
        self.rows = rows
        self.columns = columns
        self.cache = [[None for _ in range(columns)] for _ in range(rows)]
        self.default = default
        

    def __getitem__(self, key: Tuple[int, int]) -> Any:
        if (
            key[0] < 0 or key[0] >= self.rows or
            key[1] < 0 or key[1] >= self.columns
        ):
            return self.default
        
        return self.cache[key[0]][key[1]]
    

    def __setitem__(self, key: Tuple[int, int], value: Any):
        self.cache[key[0]][key[1]] = value


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = DefaultCache(2, len(prices), 0)

        cache[0, len(prices) - 1] = 0
        cache[1, len(prices) - 1] = 0
        
        for day_index in range(len(prices) - 1, -1, -1):
            # does not have stock
            cache[0, day_index] = max(
                cache[1, day_index + 1] - prices[day_index],  # buy
                cache[0, day_index + 1]                       # idle
            )
            
            # has stock
            cache[1, day_index] = max(
                cache[0, day_index + 2] + prices[day_index],  # sell
                cache[1, day_index + 1]                       # hold
            )

        return cache[0, 0]


if __name__ == "__main__":
    assert Solution().maxProfit([1,2,3,0,2]) == 3
    assert Solution().maxProfit([1]) == 0
