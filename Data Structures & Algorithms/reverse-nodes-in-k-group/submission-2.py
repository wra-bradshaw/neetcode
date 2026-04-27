# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fake_head = ListNode(-1, head)
        head_prev = fake_head

        while True:
            end_node = self.getNode(head_prev, k)
            if end_node == None:
                break
            next_node = end_node.next
            next_head_prev = head_prev.next

            self.reverseNodes(head_prev.next, next_node, k)

            head_prev.next = end_node
            head_prev = next_head_prev

        return fake_head.next


    def reverseNodes(self, head: Optional[ListNode], prev: Optional[ListNode], k: int):
        curr = head
        prev_node = prev
        i = 0

        while curr != None and i < k:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
            i += 1

    def getNode(self, head: Optional[ListNode], i: int) -> Optional[ListNode]:    
        curr = head    
        j = 0
        while curr != None and j < i:
            curr = curr.next
            j += 1
        return curr



