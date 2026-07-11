# We use a sliding window approach to find the length of the longest substring without repeating characters. 
# We maintain a dictionary to store the last index of each character and two pointers to represent the current window. 
# If we encounter a repeating character, we move the left pointer to the right of the last occurrence of that character. 
# We update the maximum length of the substring as we iterate through the string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1

            char_index[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len