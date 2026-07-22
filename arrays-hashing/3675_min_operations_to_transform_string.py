class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0

        for c in s:
            shifts = (26 - (ord(c) - ord('a'))) % 26
            ans = max(ans, shifts)

        return ans