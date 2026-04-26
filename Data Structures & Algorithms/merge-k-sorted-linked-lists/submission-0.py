# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fake_head = ListNode(-1, None)

        curr = fake_head
        while True:
            min_idx: int | None = None
            for i in range(0, len(lists)):
                min_val = lists[min_idx].val if min_idx != None else math.inf
                current_val = lists[i].val if lists[i] != None else math.inf
                
                if current_val < min_val:
                    min_idx = i
            
            if min_idx != None:
                curr.next = lists[min_idx]
                lists[min_idx] = lists[min_idx].next
                curr = curr.next
            else:
                break
                
        return fake_head.next



