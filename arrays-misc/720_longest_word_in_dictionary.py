#Approach: Sort the words lexicographically. Use a set to keep track of the words that can be built. 
# Iterate through the sorted list of words, and for each word, check if it can be built by checking if its prefix (word[:-1]) 
# is in the set. If it can be built, add it to the set and update the answer if it's longer than the current answer.

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        built = set()
        answer = ""

        for word in words:
            if len(word) == 1 or word[:-1] in built:
                built.add(word)

                if len(word) > len(answer):
                    answer = word

        return answer