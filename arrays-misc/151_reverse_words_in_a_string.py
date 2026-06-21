class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words_list = s.split()
        words_list.reverse()
        res = ' '.join(words_list)
        return res

        