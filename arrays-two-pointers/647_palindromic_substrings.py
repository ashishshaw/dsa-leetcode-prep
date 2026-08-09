# We can find all palindromic substrings by expanding around each character (for odd-length palindromes) and each pair of characters (for even-length palindromes). 
# We define a helper function that expands around a given center and counts palindromic substrings.
# Then we iterate through the string, calling this helper function for each character and each pair of characters, accumulating the count of palindromic substrings.

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(left, right):
            nonlocal count

            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            # Odd-length palindromes
            expand(i, i)

            # Even-length palindromes
            expand(i, i + 1)

        return count