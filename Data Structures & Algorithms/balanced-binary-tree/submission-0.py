# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
    
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res

            if root == None:
                return 0

            l_height = dfs(root.left)
            r_height = dfs(root.right)

            res = res and abs(l_height - r_height) <= 1
            
            return max(l_height, r_height) + 1
            
        dfs(root)

        return res
