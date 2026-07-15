#expand around center approach
#then we initialize two variables start and end to 0, which will be used to keep track of the start and end indices of the longest palindromic substring found so far.
#we define a helper function expand that takes two indices left and right as input. This function expands around the center defined by left and right, checking if the characters at those indices are equal.
#If they are equal, we continue expanding until we reach the boundaries of the string or find characters that are not equal. The function returns the updated left and right indices after expansion.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]