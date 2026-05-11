# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        res: list[int] = []

        queue: deque[tuple[int, TreeNode]] = deque([(0, root)])
        
        prevPopped: Optional[tuple[int, TreeNode]] = None 
        while len(queue) > 0:
            depth, popped = queue.popleft()

            if prevPopped and prevPopped[0] != depth:
                res.append(prevPopped[1].val)

            if popped.left != None:
                queue.append((depth + 1, popped.left))
            if popped.right != None:
                queue.append((depth + 1, popped.right))

            prevPopped = (depth, popped)

        if prevPopped:
            res.append(prevPopped[1].val)

        return res