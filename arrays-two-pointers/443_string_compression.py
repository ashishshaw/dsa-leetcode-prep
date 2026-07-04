#Approach: We use two pointers, one for reading the characters and another for writing the compressed characters. 
#We iterate through the input list, counting consecutive characters and writing the character and its count (if greater than 1) 
#to the write pointer. Finally, we return the length of the compressed list.

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write