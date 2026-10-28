#Approach: Use a min-heap to keep track of the end times of meetings.
#For each meeting, if its start time is after the earliest end time, we can reuse that room.
#Otherwise, we need a new room.

from collections import Counter
import heapq
class Solution:
    def meetingRooms(self, intervals: List[int]) -> List[int]:
        intervals.sort(key= lambda x: x[0])
        heap = []
        for start, end in intervals:

            if heap and start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

        return len(heap)
        
