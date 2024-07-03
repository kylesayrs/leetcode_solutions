from typing import List

import heapq


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        sort
        greedily choose between moving the left and right ends

        Maybe we only need to keep the top 3?
        """
        if len(nums) <= 4:
            return 0

        # get top four
        heapq.heapify(nums)
        bot_four = [
            heapq.heappop(nums)
            for _ in range(4)
        ]

        # reconstruct nums
        nums += bot_four

        # invert values to get bottom four
        for index in range(len(nums)):
            nums[index] = -nums[index]
        heapq.heapify(nums)
        top_four = [
            -heapq.heappop(nums)
            for _ in range(4)
        ]

        # two approaches, we can either implement a greedy thing
        # or just search all the possible choices

        # EDIT: actually, the greedy strategy doesn't work, imagine
        # bot=[0, 0, 1000] top=[1000, 1010, 1020]

        print(top_four)
        print(bot_four)
        
        # search through all possible options of choosing left and right
        return min(top_four[i] - bot_four[3 - i] for i in range(4))
