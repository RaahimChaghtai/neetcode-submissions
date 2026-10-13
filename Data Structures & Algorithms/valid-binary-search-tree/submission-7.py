# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to recursively validate each node against a valid value range
        def isValid(node, minn, maxx):
            # Base case: If we've reached a leaf's child (None), that branch is valid
            if not node:
                return True
            
            # Violation check: The current node's value must strictly stay 
            # within the allowed minimum and maximum boundaries
            if node.val <= minn or node.val >= maxx:
                return False
            
            # Recursive step:
            # 1. When going LEFT, the maximum boundary updates to node.val 
            #    (because nothing in the left subtree can be greater than or equal to the current root)
            # 2. When going RIGHT, the minimum boundary updates to node.val 
            #    (because nothing in the right subtree can be smaller than or equal to the current root)
            return (isValid(node.left, minn, node.val) and 
                    isValid(node.right, node.val, maxx))
        
        # Kick off the recursion starting at the root, 
        # initially allowing any value between negative and positive infinity
        return isValid(root, float("-inf"), float("inf"))