#Time complexity: O(n * k) -> For n words and each word of length k
# 1. Create a dp array of size n+1 and initialize it with False
# 2. Set dp[0] to True, as an empty string can be segmented
# 3. Iterate through the string from index 1 to n, and for each index
#    a. Iterate through the string from index 0 to i, and check if dp[j] is True and s[j:i] is in wordDict
#    b. If both conditions are satisfied, set dp[i] to True and break the inner loop
# 4. Finally, return dp[-1] which will indicate if the entire string can be segmented or not


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)

        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[-1]