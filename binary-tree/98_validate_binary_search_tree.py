#Approach: In-Order Traversal
#First, we perform an in-order traversal of the binary tree and store the values in a list.
# Then, we check if the list is sorted in ascending order. 

# Input: root = [2,1,3]
# Output: true

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node, low, high):
            if node is None:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return (
                validate(node.left, low, node.val)
                and
                validate(node.right, node.val, high)
            )
        
        return validate(root, float("-inf"), float("inf"))