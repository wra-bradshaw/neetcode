# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> Optional[int]:
        stack = []
        current: Optional[TreeNode] = root
        i = 0

        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            i += 1
            if i == k and current:
                return current.val
            
            current = current.right if current != None else None
            
        return None