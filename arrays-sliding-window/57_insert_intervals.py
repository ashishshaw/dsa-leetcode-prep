#check if the new interval overlaps with any existing intervals and merge them if necessary. The algorithm works in three main steps:
# 1. Add all intervals that come before the new interval (i.e., intervals that end before the new interval starts) to the result list.
# 2. Merge all overlapping intervals with the new interval. This is done by updating the start and end of the new interval to encompass all overlapping intervals.
# 3. Add all intervals that come after the new interval (i.e., intervals that start after the new interval ends) to the result list.
# Finally, return the result list containing the merged intervals.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # Add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        # Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res