# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        if subRoot == None:
            return True
        if root == None:
            return False
        return self.sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, root: Optional[TreeNode], other: Optional[TreeNode]):
        if root == None and other == None:
            return True
        if root == None or other == None:
            return False

        return root.val == other.val and self.sameTree(root.left, other.left) and self.sameTree(root.right, other.right)
