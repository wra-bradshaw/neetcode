# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.list_len(head)
        idx = length - n
        fake_head = ListNode(-1, head)

        prev = fake_head
        i = 0
        while prev.next:
            curr = prev.next

            if i == idx:
                prev.next = curr.next
                break

            prev = curr
            i += 1
        
        return fake_head.next

    def list_len(self, head: Optional[ListNode]) -> int:
        i = 0
        while head:
            i += 1
            head = head.next
        return i
        