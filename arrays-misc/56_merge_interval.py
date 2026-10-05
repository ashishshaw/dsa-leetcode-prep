#check if the current interval overlaps with the last merged interval 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    
    #Alternate approach: Sort the intervals based on the start time and then iterate through the intervals, merging them if they overlap.
    intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

    intervals.sort(key=lambda x: x[0])
    
    res = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])

    print(res)