#Approach: Stack
#We use a stack to keep track of indices of the histogram bars in increasing order of their heights.
#When we encounter a bar with a smaller height, we pop bars from the stack and calculate the area of the rectangle formed by the popped bar.

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # indices
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                left = stack[-1] if stack else -1
                width = i - left - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        # Process remaining bars
        n = len(heights)
        while stack:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = n - left - 1

            max_area = max(max_area, height * width)

        return max_area