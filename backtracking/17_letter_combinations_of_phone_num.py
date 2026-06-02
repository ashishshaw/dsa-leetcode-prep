# Define cases where it needs to stop (return)
# Backtracking std: Choose, Backtrack, Pop
    
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return

        res = []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, path):

            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            curr_digit = digits[index]
            letters = phone_map[curr_digit]
        
            for letter in letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()


        backtrack(0, [])
        return res
        