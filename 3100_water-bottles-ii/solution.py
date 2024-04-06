class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drank = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            total_drank += 1
            empty_bottles += 1 - numExchange
            numExchange += 1

        return total_drank
    

    def maxBottlesDrunk_optimized(self, numBottles: int, numExchange: int) -> int:
        original_numExchange = numExchange
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            empty_bottles += 1 - numExchange
            numExchange += 1

        return numBottles + numExchange - original_numExchange
    

if __name__ == "__main__":
    assert Solution().maxBottlesDrunk(10, 3) == 13
