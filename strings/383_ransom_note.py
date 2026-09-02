#Approach: Use a Counter to count the frequency of each character in the ransomNote and magazine.
# Then, check if for every character in ransomNote, the count in magazine is greater than or equal to the count in ransomNote. 
#If it is, return True; otherwise, return False

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        return all(m[c] >= count for c, count in r.items())