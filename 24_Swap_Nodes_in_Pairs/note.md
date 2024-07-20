# first time
I finish the question by watching https://www.bilibili.com/video/BV1YT411g7br/

<font color="red">need to do this again!!</font>

the process are as follows:
>+ (1) define a dummynode, and use a ListNode named cur, we init cur=dummynode
>+ (2) we need to change cur.next and cur.next.next, before swap them, we need to identify whether they are exists
>+ (3) do the following process ![picture](./picture.png)
>+ for 1 and 3, use var temp to store them

# second time
done it by myself in 12 min. don't need to do another time.

# 7.20日重刷第一遍
还是可以想到原来的过程的，分为好几步， 思路什么都没问题
然后还发现了上述的三步走可以第一步和第二部互换，不同的就是使用temp储存第一个节点还是第二个节点的问题

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
```