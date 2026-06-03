# Two points with distance multiplied by shortest tower

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        curr = 0
        while left < right:
            curr = (right-left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if curr > max_area:
                max_area = curr
        
        return max_area
        