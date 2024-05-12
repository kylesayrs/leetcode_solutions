from typing import List

import math
from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        earn_values = defaultdict(lambda: 0)
        for num in nums:
            earn_values[num] += num
        #print(earn_values)

        num_keys = list(sorted(earn_values.keys()))

        prev_earn = 0
        pred_earn = 0
        for index, num in enumerate(num_keys):
            max_earn = max(prev_earn + earn_values[num], pred_earn)
            #print(f"num: {num}, max_earn: {max_earn}, prev_earn: {prev_earn}, pred_earn: {pred_earn}")

            if index + 1 < len(num_keys) and num_keys[index + 1] == num + 1:
                prev_earn = pred_earn
                pred_earn = max_earn

            else:
                prev_earn = max_earn
                pred_earn = max_earn

        return max(prev_earn, pred_earn)


if __name__ == "__main__":
    # Solution().deleteAndEarn([3,4,2])
    # Solution().deleteAndEarn([2,2,3,3,3,4])
    # Solution().deleteAndEarn([2, 10, 5])
    assert Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6]) == 18
