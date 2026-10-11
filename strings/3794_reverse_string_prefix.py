#Input: s = "abcd", k = 2
# Output: "bacd"

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]