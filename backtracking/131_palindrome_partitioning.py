#Check if the current substring is a palindrome then add it to the path and backtrack to find the next substring. 
# If the start index is equal to the length of the string, then we have found a valid partition and add it to the result.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                curr = s[start:end + 1]

                if is_palindrome(curr):
                    path.append(curr)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res