

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        max_side = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    curr[j] = 1 + min(
                        prev[j],      # top
                        curr[j - 1],  # left
                        prev[j - 1]   # diagonal
                    )
                    max_side = max(max_side, curr[j])
                else:
                    curr[j] = 0

            prev = curr[:]
            curr = [0] * (n + 1)

        return max_side * max_side