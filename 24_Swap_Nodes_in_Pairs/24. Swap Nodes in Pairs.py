# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#第一二步互换也可以，注释掉的是第一种，没有注释的是第二种
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        dummyhead=ListNode(next=head) 
        cur = dummyhead

        while cur.next and cur.next.next:
            temp_last = cur.next.next.next
            # the first step
            # temp_first = cur.next

            # cur.next = cur.next.next
            # cur.next.next = temp_first
            # cur.next.next.next = temp_last
            # cur = cur.next.next
            
            temp_second = cur.next.next
            cur.next.next.next = cur.next
            cur.next = temp_second
            cur.next.next.next = temp_last
            cur = cur.next.next
        
        return dummyhead.next


        