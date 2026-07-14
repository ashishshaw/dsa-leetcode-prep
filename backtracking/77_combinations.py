#check if we can generate all combinations of k numbers from 1 to n using backtracking.
#then we can use a recursive function to generate the combinations. The function will take the current combination, 
#the starting number, and the remaining numbers to choose from. If the current combination has k numbers, 
#we add it to the result list. Otherwise, we iterate through the remaining numbers and recursively call the function with the updated combination and starting number.


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start, path):
            if len(path) == k:
                ans.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack(1, [])
        return ans