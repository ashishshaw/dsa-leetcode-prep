#Two pointers approach
#Indexing is 1-based, so we return left + 1 and right + 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]

            if s == target:
                return [left + 1, right + 1]  # 1-indexed
            elif s < target:
                left += 1
            else:
                right -= 1
        