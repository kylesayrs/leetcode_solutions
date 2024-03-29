from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 0:
            return 0
        
        intervals.sort(key=lambda interval: interval[0])

        num_remove = 0
        current_interval_right = intervals[0][1]
        for interval in intervals[1:]:

            if interval[0] < current_interval_right:
                # keep whichever interval takes up less space on the right
                current_interval_right = min(current_interval_right, interval[1])
                num_remove += 1

            else:
                current_interval_right = interval[1]

        return num_remove


if __name__ == "__main__":
    solution = Solution()

    solution.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])
