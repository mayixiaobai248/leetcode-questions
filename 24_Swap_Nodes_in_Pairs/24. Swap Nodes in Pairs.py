# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node=ListNode(next=head)
        cur=dummy_node
        while cur.next and cur.next.next:
            temp1=cur.next #the first node
            temp2=cur.next.next.next #the third node
            cur.next=cur.next.next
            cur.next.next=temp1
            temp1.next=temp2
            cur=cur.next.next
        
        return dummy_node.next


        