# We can use two pointers to find if there exist two integers a and b such that a^2 + b^2 = c. 
# We initialize one pointer at 0 (left) and the other pointer at the integer square root of c (right). 
# We then calculate the sum of squares of the two pointers. If the sum is equal to c, we return True. 
# If the sum is less than c, we increment the left pointer. If the sum is greater than c, we decrement the right pointer. 
# We continue this process until the left pointer is greater than the right pointer.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.isqrt(c)

        while left <= right:
            total = left * left + right * right

            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1

        return False