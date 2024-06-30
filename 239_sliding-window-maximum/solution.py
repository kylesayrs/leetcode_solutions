from typing import List

import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        max_queue = collections.deque()  # monotonically decreasing

        result = []
        for right in range(len(nums)):
            # keep queue decreasing
            while len(max_queue) > 0 and nums[right] > nums[max_queue[-1]]:
                max_queue.pop()

            max_queue.append(right)

            if right >= k:
                if left > max_queue[0]:
                    max_queue.popleft()

            if right + 1 >= k:
                result.append(nums[max_queue[0]])
                left += 1
                
        return result
