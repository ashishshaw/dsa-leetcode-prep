#Approach: Use a stack to evaluate the expression. Iterate through the string, building numbers and applying signs. 
# When encountering '(', push the current result and sign onto the stack, and reset them for the new sub-expression. 
# When encountering ')', pop from the stack to combine the sub-expression result with the previous context.

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        sign = 1
        num = 0
        stack = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch in "+-":
                result += sign * num
                num = 0
                sign = 1 if ch == "+" else -1

            elif ch == "(":
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif ch == ")":
                result += sign * num
                num = 0

                result *= stack.pop()   # sign before '('
                result += stack.pop()   # result before '('

        return result + sign * num