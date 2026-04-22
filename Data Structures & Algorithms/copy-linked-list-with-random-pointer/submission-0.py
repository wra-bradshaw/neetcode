"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        old_to_new: dict[Node, Node] = {}

        dummy = Node(-1, head, None)
        curr = dummy

        while curr.next:
            new_node = Node(curr.next.val, curr.next.next, curr.next.random)
            old_to_new[curr.next] = new_node
            curr.next = new_node
            curr = curr.next

        curr = dummy
        while curr.next:
            if curr.next.random in old_to_new:
                curr.next.random = old_to_new[curr.next.random]

            curr = curr.next

        return dummy.next
        