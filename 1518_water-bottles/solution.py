class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        num_drank = numBottles
        num_empty = numBottles
        while True:
            num_returned = num_empty // numExchange
            if num_returned > 0:
                num_drank += num_returned
                num_empty += num_returned - num_returned * numExchange
            else:
                break

        return num_drank
