# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        orderMap: dict[int, int] = {}
        for i in range(len(inorder)):
            orderMap[inorder[i]] = i
        print(orderMap)
        
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.insert(preorder[i], root, orderMap)
        return root

    def insert(self, itm: int, root: TreeNode, orderMap: dict[int, int]):
        prev = None
        curr = root
        while curr != None:   
            if orderMap[itm] < orderMap[curr.val]:
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = TreeNode(itm)
                    return
            else:
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = TreeNode(itm)
                    return