class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]     # One valid way to finish

            if start in memo:
                return memo[start]

            res = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    suffixes = dfs(end)

                    for sentence in suffixes:
                        if sentence == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sentence)

            memo[start] = res
            return res

        return dfs(0)