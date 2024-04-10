from typing import List

import math
import heapq


class Solution:
    def l2_norm(point_a: List[int]):
        return math.sqrt(point_a[0] * point_a[0] + point_a[1] * point_a[1])
    

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        entries = [
            (Solution.l2_norm(point), point)
            for point in points
        ]

        heapq.heapify(entries)

        return [
            heapq.heappop(entries)[1]
            for _ in range(k)
        ]
    

if __name__ == "__main__":
    assert Solution().kClosest([[10, 10], [1, 1]], 1) == [[1, 1]]
    assert Solution().kClosest([[1,3],[-2,2]], 1) == [[-2,2]]
    assert Solution().kClosest([[3,3],[5,-1],[-2,4]], 2) == [[3,3],[-2,4]]
