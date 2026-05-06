# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        return max(left + right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))