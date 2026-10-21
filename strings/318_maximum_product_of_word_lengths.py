#Approach: Use bit manipulation to represent the presence of characters in each word. 
# For each pair of words, check if their bitmasks have no common bits (i.e., they share no common characters).

class Solution:
    def maxProduct(self, words: list[str]) -> int:
        masks = []

        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks.append(mask)

        ans = 0
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans