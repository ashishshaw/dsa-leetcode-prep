#check if the string contains all the characters of the target string and return the minimum window substring
#then we can use a sliding window approach to find the minimum window substring. 
# We can use a counter to keep track of the characters in the target string and a variable 
# to keep track of the number of characters that are still needed. We can then iterate through the string, 
# expanding the window until we have all the characters, and then contracting the window until we no longer have all the characters. 
# We can keep track of the minimum window substring as we go.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if end == 0 or right - left < end - start:
                    start, end = left, right

                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]