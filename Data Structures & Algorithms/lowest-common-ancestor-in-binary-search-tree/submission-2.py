# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # RECURSIVE - O(H)
        # If both p and q are greater than root, LCA must be in the right subtree
        # if root.val < p.val and root.val < q.val:
            # return self.lowestCommonAncestor(root.right, p, q)
        
        # If both p and q are smaller than root, LCA must be in the left subtree
        # if root.val > p.val and root.val > q.val:
            # return self.lowestCommonAncestor(root.left, p, q)
        
        # Otherwise, they have split (or one of them is the root itself)! 
        # This current root is the Lowest Common Ancestor.
        # return root

        # ITERATIVE -
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr
                
            