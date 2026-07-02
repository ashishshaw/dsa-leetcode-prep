#Check if the current number has been seen before, if yes then it is not a happy number
#Then calculate the sum of the squares of the digits of the number and repeat 
# the process until we reach 1 or a number that has been seen before.

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))

        return n == 1