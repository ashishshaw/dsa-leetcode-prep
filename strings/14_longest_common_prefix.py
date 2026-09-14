#Approach: Sort the array of strings and then compare the first and last strings in the sorted array. 
#The common prefix of these two strings will be the longest common prefix for the entire array.

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = strs[0]

        for items in strs[1:]:
            while not items.startswith(prefix):
                prefix = prefix[:-1]

        return prefix

