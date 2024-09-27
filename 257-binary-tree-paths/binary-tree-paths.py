# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(root, path):
            if not root:
                return None
            
            if path:
                path += "->" + str(root.val)
            else:
                path += str(root.val)
                
            if not root.right and not root.left:
                res.append(path)
                return
            
            dfs(root.left, path)
            dfs(root.right, path)
            
        dfs(root, "")
        return res