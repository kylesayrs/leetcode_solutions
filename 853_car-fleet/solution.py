from typing import List

import math


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed), key=lambda p_s: p_s[0]))
        fleet_times_to_target = []

        for index in reversed(range(len(position))):
            time_to_target = (target - position[index]) / speed[index]
            if (
                len(fleet_times_to_target) <= 0 or
                time_to_target > fleet_times_to_target[-1]
            ):
                fleet_times_to_target.append(time_to_target)

        return len(fleet_times_to_target)
    

if __name__ == "__main__":
    assert Solution().carFleet(10, [0, 1], [1, 1]) == 2
    assert Solution().carFleet(10, [0, 1], [2, 1]) == 1
    assert Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
    assert Solution().carFleet(10, [3], [3]) == 1
    assert Solution().carFleet(100, [0,2,4], [4,2,1]) == 1
    assert Solution().carFleet(10, [6,8], [3,2]) == 2
    assert Solution().carFleet(10, [0,4,2], [2,1,3]) == 1
    assert Solution().carFleet(16, [11,14,13,6], [2,2,6,7]) == 2
