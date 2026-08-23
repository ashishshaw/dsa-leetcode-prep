#Approach: Use the Sieve of Eratosthenes algorithm to count the number of prime numbers less than n.
#First, create a boolean array is_prime of size n initialized to True.
#Then, iterate through the numbers starting from 2 and mark all multiples of each prime number as False in the is_prime array.
#Finally, return the count of True values in the is_prime array, which represents the number of prime numbers less than n.

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        p = 2

        while p * p < n:
            if is_prime[p]:
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
            p += 1

        return sum(is_prime)