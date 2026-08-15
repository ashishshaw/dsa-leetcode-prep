#Approach: Use a stack to keep track of the current string and the number of times it should be repeated. 
# Iterate through the input string character by character, and when encountering a digit, build the current number. 
# When encountering an opening bracket '[', push the current string and number onto the stack and reset them. 
# When encountering a closing bracket ']', pop from the stack and repeat the current string accordingly. 
# Finally, return the constructed string.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                curr_str += ch

        return curr_str