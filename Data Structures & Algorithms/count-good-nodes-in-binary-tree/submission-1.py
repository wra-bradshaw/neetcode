# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        n_good_nodes: int = 0

        def dfs(root: Optional[TreeNode], max_en_route: int):
            nonlocal n_good_nodes;

            if root == None:
                return 0
            if root.val >= max_en_route:
                n_good_nodes += 1
                max_en_route = root.val

            dfs(root.left, max_en_route)
            dfs(root.right, max_en_route)
        
        dfs(root, float(-sys.maxsize))

        return n_good_nodes