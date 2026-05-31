class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {"]":"[", ")":"(","}":"{"}
        stack = []
        for ch in s:
            if ch in char_map:
                if not stack or stack.pop() != char_map[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
        