#Approach: Use a stack to build the result string. 
#Keep track of the last occurrence of each character and a set to check if a character is already in the stack.
#Find the lexicographically smallest subsequence without duplicates.

# Input: s = "cbacdcbc"
# Output: "acdb"

# Input: s = "bcabc"
# Output: "abc"

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue

            while stack and c < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return ''.join(stack)