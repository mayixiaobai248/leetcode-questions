# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        privalue=0 
        cur=dummy=ListNode()
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 and l2:
            cur.next=ListNode((l1.val+l2.val+privalue)%10)
            privalue=int((l1.val+l2.val+privalue)/10)     

            l1=l1.next
            l2=l2.next
            cur=cur.next

        if l1:
            while l1:
                cur.next=ListNode((l1.val+privalue)%10)
                privalue=int((l1.val+privalue)/10)   
                l1=l1.next
                cur=cur.next

        if l2:
            while l2:
                cur.next=ListNode((l2.val+privalue)%10)
                privalue=int((l2.val+privalue)/10)  
                l2=l2.next
                cur=cur.next

        if privalue==1:
            cur.next=ListNode(privalue)
        
        return dummy.next
