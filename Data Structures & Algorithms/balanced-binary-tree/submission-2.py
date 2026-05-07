class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            l_height = dfs(node.left)
            if l_height == -1:       
                return -1

            r_height = dfs(node.right)
            if r_height == -1:       
                return -1

            if abs(l_height - r_height) > 1:
                return -1 
            
            return max(l_height, r_height) + 1
            
        return dfs(root) != -1