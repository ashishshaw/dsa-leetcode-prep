#Check if the number is the start of a sequence, then check for the next numbers in the sequence
#Seemple: [100, 4, 200, 1, 3, 2] -> 1 is the start of a sequence, check for 2, then 3, then 4. The length of the sequence is 4.
#See if num - 1 is in the set, if not, then it is the start of a sequence. Then check for num + 1, num + 2, etc. until the next number is not in the set. Keep track of the length of the sequence and update the result if it is greater than the previous result.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                curr = num
                length = 1

                while curr + 1 in nums:
                    length += 1
                    curr += 1
            
                res = max(res, length)

        return res