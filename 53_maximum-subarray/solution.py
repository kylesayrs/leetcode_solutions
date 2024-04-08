from typing import Tuple, List, Any

import math


class DefaultCache:
    def __init__(self, rows: int, columns: int, default):
        self.rows = rows
        self.columns = columns
        self.default = default

        self.cache = [[None for _ in range(columns)] for _ in range(rows)]


    def __getitem__(self, key: Tuple[int, int]):
        if (
            key[0] < 0 or key[0] >= self.rows or
            key[1] < 0 or key[1] >= self.columns
        ):
            return self.default

        return self.cache[key[0]][key[1]]
    

    def __setitem__(self, key: Tuple[int, int], value: Any):
        self.cache[key[0]][key[1]] = value


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixes = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            prefixes.append(prefix_sum)

        cache = DefaultCache(3, len(prefixes) + 1, -math.inf)
        
        cache[0, len(prefixes)] = -math.inf
        cache[1, len(prefixes)] = -math.inf
        cache[2, len(prefixes)] = 0

        for index in reversed(range(len(prefixes))):
            # has ended right
            cache[2, index] = cache[2, index + 1]

            # has started left
            cache[1, index] = max(
                cache[1, index + 1],               # continue not ending right
                cache[2, index] + prefixes[index]  # end right
            )

            # has not started left
            cache[0, index] = max(
                cache[0, index + 1],                   # continue not starting left
                cache[1, index + 1] - prefixes[index]  # start left
            )

        return max(cache[0, 0], cache[1, 0])
    

    def maxSubArray(self, nums: List[int]) -> int:
        prefixes = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            prefixes.append(prefix_sum)

        prev_not_started_left = -math.inf
        prev_started_left = -math.inf
        prev_ended_right = 0

        for prefix in reversed(prefixes):
            # has ended right
            ended_right = prev_ended_right

            # has started left
            started_left = max(
                prev_started_left,         # continue not ending right
                ended_right + prefix  # end right
            )

            # has not started left
            not_started_left = max(
                prev_not_started_left,      # continue not starting left
                prev_started_left - prefix  # start left
            )

            prev_not_started_left = not_started_left
            prev_started_left = started_left
            prev_ended_right = ended_right

        return max(prev_not_started_left, prev_started_left)
    
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array = nums[0]

        prev_sum = 0
        for num in nums:
            prev_sum = max(prev_sum, 0)

            _sum = prev_sum + num
            max_sub_array = max(max_sub_array, _sum)

            prev_sum = _sum

        return max_sub_array


if __name__ == "__main__":
    assert Solution().maxSubArray([1]) == 1
    assert Solution().maxSubArray([1, 2]) == 3
    assert Solution().maxSubArray([1, 2]) == 3
    assert Solution().maxSubArray([5,4,-1,7,8]) == 23
    assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert Solution().maxSubArray([-1]) == -1
