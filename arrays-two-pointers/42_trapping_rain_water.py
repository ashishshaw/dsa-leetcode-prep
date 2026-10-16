#Approach: First, we use two pointers to traverse the array from both ends. 
#We keep track of the maximum height seen so far from both sides. 
#At each step, we move the pointer with the smaller height and update the water trapped based on the difference 
#between the current height and the maximum height seen so far.

#                                |"""|                    
#                                |___|                    
#            |"""|~~~~~~~~~~~~~~~|"""||"""|~~~~~|"""|     
#            |___|               |___||___|     |___|     
#  |"""|~~~~~|"""||"""|~~~~~|"""||"""||"""||"""||"""||"""|
#  |___|     |___||___|     |___||___||___||___||___||___|

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        water = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]

                left += 1

            else:

                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]

                right -= 1

        return water