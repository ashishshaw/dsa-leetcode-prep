#Approach: Use a Counter to keep track of the maximum frequency of each character required by words2.
# Then, for each word in words1, check if it contains at least the required frequency of each character. If it does, add it to the result list.


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = Counter()

        for word in words2:
            freq = Counter(word)
            for ch, count in freq.items():
                required[ch] = max(required[ch], count)

        # A word is universal if it contains all required characters
        ans = []

        for word in words1:
            freq = Counter(word)
            if all(freq[ch] >= count for ch, count in required.items()):
                ans.append(word)

        return ans