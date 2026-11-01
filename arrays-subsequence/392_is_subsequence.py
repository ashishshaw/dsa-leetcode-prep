#Approach: Use two pointers to traverse both strings and check if s is a subsequence of t.

# Input: s = "abc", t = "ahbgdc"
# Output: true

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        
        return i == len(s)