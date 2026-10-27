#Approach: Use a min-heap of size k to keep track of the k largest elements.
#For each element in the array, if it's larger than the smallest element in the heap, replace smallest element with current one.
#The root of the min-heap will be the kth largest element.

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
 