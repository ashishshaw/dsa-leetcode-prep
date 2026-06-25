#boyer-Moore Voting Algorithm
#Count -> 1 whenever new candidate is found, decrement count when a different number is found. 
# When count reaches 0, we have a new candidate. The majority element will be the last candidate remaining.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for num in nums[1:]:

            if candidate == num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = num
                    count += 1

        return candidate
        