#Approach: Use backtracking to place queens on the board. Keep track of the columns and diagonals that are already occupied by queens. 
# For each row, try placing a queen in each column and check if it's safe (i.e., not in the same column or diagonal as any previously placed queen). 
# If it's safe, place the queen and move to the next row. If all queens are placed successfully, increment the count of valid solutions. 
# Backtrack by removing the queen and trying the next column.

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(row):
            if row == n:
                return 1

            count = 0
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                count += backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return count

        return backtrack(0)