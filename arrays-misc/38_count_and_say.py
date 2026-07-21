#Approach: We start with the base case "1" and iteratively build the next term by counting consecutive digits in the current term. 
# For each digit, we keep track of its count and append the count followed by the digit to form the next term. 
# We repeat this process n-1 times to get the nth term.

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            res = []
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(s[i - 1])
                    count = 1

            # Last group
            res.append(str(count))
            res.append(s[-1])

            s = "".join(res)

        return s