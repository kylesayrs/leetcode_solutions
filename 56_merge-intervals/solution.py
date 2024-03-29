from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 0:
            return []

        intervals.sort(key=lambda interval: interval[0])

        merged_intervals = []
        merge_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] > merge_interval[1]:
                merged_intervals.append(merge_interval)
                merge_interval = interval

            else:
                merge_interval[1] = max(merge_interval[1], interval[1])

        merged_intervals.append(merge_interval)

        return merged_intervals
