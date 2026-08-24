#Approach: Use bit manipulation to find the two unique numbers. First, XOR all the numbers in the array to get the XOR of the two unique numbers. 
# Then, find a bit that is set in the XOR result, which indicates that the two unique numbers differ at that bit position. 
# Finally, divide the numbers into two groups based on that bit and XOR each group to find the two unique numbers.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        # XOR of the two unique numbers
        for num in nums:
            xor ^= num

        # Get a bit where the two unique numbers differ
        diff = xor & -xor

        a = 0
        b = 0

        # Divide numbers into two groups using that bit
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]