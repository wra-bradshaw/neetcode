# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -sys.maxsize

        def dfs(root: Optional[TreeNode]):
            if root == None:
                return 0

            nonlocal maxSum

            leftSum = dfs(root.left)
            rightSum = dfs(root.right)

            print(root.val, leftSum, rightSum)

            pathSum = leftSum + rightSum + root.val
            if pathSum > maxSum:
                maxSum = pathSum

            return max(root.val + leftSum, root.val + rightSum, 0)

        dfs(root)

        return maxSum

