# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA=0
        lenB=0
        temp1=headA
        temp2=headB
        while temp1:
            temp1=temp1.next
            lenA=lenA+1
        while temp2:
            temp2=temp2.next
            lenB=lenB+1
        
        temp1=headA
        temp2=headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                temp1=temp1.next
        if lenA<lenB:
            for i in range(lenB-lenA):
                temp2=temp2.next

        for i in range(min(lenA,lenB)):
            # if temp1.val==temp2.val:
            if temp1==temp2:
                return temp1
            else:
                temp1=temp1.next
                temp2=temp2.next
    
        return None