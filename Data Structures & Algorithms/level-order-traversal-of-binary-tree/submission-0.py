# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        res: List[List[int]] = []
        queue: deque[tuple[int, TreeNode]] = deque([(0, root)])
        level = 0
        
        while len(queue) > 0:
            depth, popped = queue.popleft()

            if depth + 1 > len(res):
                res.append([popped.val])
            else:
                res[depth].append(popped.val)
            
            if popped.left:
                level += 1
                queue.append((depth + 1, popped.left))
            if popped.right:
                queue.append((depth + 1, popped.right))

            print(popped.val)

        return res





        