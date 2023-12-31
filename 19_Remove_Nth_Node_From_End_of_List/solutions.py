# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head=ListNode(next=head)
        slow=dummy_head
        fast=slow
        for i in range(n+1):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        #slow.next is the node need to remove
        slow.next=slow.next.next
        return dummy_head.next



        