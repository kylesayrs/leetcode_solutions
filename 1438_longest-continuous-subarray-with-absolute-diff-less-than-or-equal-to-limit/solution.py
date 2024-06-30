from typing import List

from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()  # decreasing
        min_queue = deque()  # increasing

        longest = 0
        left = 0
        for right in range(len(nums)):
            # maintain properties
            while len(max_queue) > 0 and nums[right] > nums[max_queue[-1]]:
                max_queue.pop()
            while len(min_queue) > 0 and nums[right] < nums[min_queue[-1]]:
                min_queue.pop()

            # append to queue
            max_queue.append(right)
            min_queue.append(right)

            # move left pointer
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if left >= max_queue[0]:  # can also compare values
                    max_queue.popleft()
                if left >= min_queue[0]:  # can also compare values
                    min_queue.popleft()

                left += 1

            # save longest
            longest = max(longest, right - left + 1)

        return longest
