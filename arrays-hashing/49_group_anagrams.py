# 1st approach: O(n * k log k) -> For n words and sorting each word of length k
# 2nd approach: O(n * k) -> Sorting avoided

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            res[key].append(word)

        return list(res.values())
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1

            groups[tuple(count)].append(s)

        return list(groups.values())
