# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        root.right = self.pruneTree(root.right)
        root.left = self.pruneTree(root.left)
        
        if root.val == 0 and not root.left and not root.right:
            return None
        else:
            return root