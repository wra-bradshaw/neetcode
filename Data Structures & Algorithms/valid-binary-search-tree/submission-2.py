# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        is_valid = True

        def dfs(root: TreeNode | None, greater_than: int, less_than: int):
            nonlocal is_valid

            if root == None:
                return True

            return root.val > greater_than and root.val < less_than and dfs(root.left, greater_than, root.val) and dfs(root.right, root.val, less_than)

        return dfs(root, -sys.maxsize, sys.maxsize)
            