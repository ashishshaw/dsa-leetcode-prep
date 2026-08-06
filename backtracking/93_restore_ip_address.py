#first we define a helper function backtrack that takes the current starting index in the string and the current path of segments.
#If the path has 4 segments and we have consumed the entire string, we join the segments with dots and add it to the result list. 
# Otherwise, we iterate through possible segment lengths (1 to 3) and check if the segment is valid (not starting with '0' 
# unless it's '0' and less than or equal to 255). If valid, we add the segment to the path and recursively call backtrack for the next segment. 
# After returning from recursion, we remove the last segment to backtrack and explore other possibilities. 
#Finally, we return the result list containing all valid IP addresses. 

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) > 255:
                    continue

                path.append(part)
                backtrack(start + length, path)
                path.pop()

        backtrack(0, [])
        return res