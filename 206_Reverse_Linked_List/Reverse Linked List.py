# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy_head=ListNode(next=head)
        #init two pointers
        # pre=dummy_head
        pre=None
        cur=head
        while cur:
            temp=cur.next #store the next number
            cur.next=pre
            pre=cur
            cur=temp
        return pre