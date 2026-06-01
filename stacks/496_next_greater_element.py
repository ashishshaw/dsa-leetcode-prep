#stack and hashmap only for nums2

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge = {}

        for i, num in enumerate(nums2):
            while stack and num > stack[-1]:
                nge[stack.pop()] = num

            stack.append(num)

        while stack:
            nge[stack.pop()] = -1

        return [nge[num] for num in nums1]
