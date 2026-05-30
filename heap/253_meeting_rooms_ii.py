#Rooms not required if current start >= end 


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
        
