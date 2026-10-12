# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]

        def dfs(root):
            if not root:
                return None
            
            lca[0] = root
            if root is p or root is q:
                return 
            elif root.val < p.val and root.val < q.val:
                dfs(root.right)
            elif root.val > p.val and root.val > q.val:
                dfs(root.left)
            else:
                return
        
        dfs(root)
        return lca[0]

            