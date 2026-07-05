#Then we create a counter for p and a counter for the first window of s with the same length as p. We compare the two counters, 
#if they are equal, we add the starting index of the window to the answer list. We then slide the window by one character at a time, 
#updating the counter for the window and comparing it to the counter for p. 
#If they are equal, we add the starting index of the window to the answer list. Finally, we return the answer list.

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        need = Counter(p)
        window = Counter(s[:len(p)])

        ans = []

        if window == need:
            ans.append(0)

        for i in range(len(p), len(s)):
            window[s[i]] += 1
            window[s[i-len(p)]] -= 1

            if window[s[i-len(p)]] == 0:
                del window[s[i-len(p)]]

            if window == need:
                ans.append(i-len(p)+1)

        return ans