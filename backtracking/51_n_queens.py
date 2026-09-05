# For each row, try placing a queen in each column and check if it's safe (no other queens in the same column or diagonals).
# If it's safe, place the queen and move to the next row. If we reach the last row, we found a valid solution and add it to the result. 
# After exploring that path, backtrack by removing the queen and trying the next column.

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(r):

            # We successfully placed queens in all rows
            if r == n:
                result.append(
                    ["".join(row) for row in board]
                )
                return

            # Try every column in this row
            for c in range(n):

                # Is this position safe?
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                # PLACE
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                # GO TO NEXT ROW
                backtrack(r + 1)

                # UNDO
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)

        return result
