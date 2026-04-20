# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        midpoint = self.split(head)
        midpoint = self.reverse(midpoint)

        p1 = head
        p2 = midpoint

        while p1 and p2:
            tmp1 = p1.next
            tmp2 = p2.next

            p1.next = p2
            p2.next = tmp1

            p2 = tmp2
            p1 = tmp1
        
        return
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: 
            return head

        prev_node = None
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        
        return prev_node

    def split(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
        slow = head
        fast = head.next

        prev = None
        while fast and fast.next and slow and slow.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        
        return second_half
