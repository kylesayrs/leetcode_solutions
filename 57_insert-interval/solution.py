from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []

        for index, interval in enumerate(intervals):
            if newInterval is None:
                new_intervals.append(interval)
                continue

            # to the right
            if newInterval[0] > interval[1]:
                new_intervals.append(interval)
                continue

            # to the left
            if newInterval[1] < interval[0]:
                new_intervals.append(newInterval)
                new_intervals.append(interval)
                newInterval = None
                continue

            # merge
            interval[0] = min(interval[0], newInterval[0])
            interval[1] = max(interval[1], newInterval[1])
            newInterval = interval

        if newInterval is not None:
            new_intervals.append(newInterval)

        return new_intervals
    

if __name__ == "__main__":
    assert Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert Solution().insert([], [4,8]) == [[4,8]]
