# first time
use two var and change the directions

<font color='red'>can do it again</font>

I first use dummynode to do this, but it shows that there is a circle.
so **pre must be null(because it is the final ListNode->next)**

# second time

can do it by myself, but there is one thing:

pre=None instead of pre=ListNode(None)

# 7.20 重刷第一遍
看了代码随想录的解析知道要用两个指针去储存，剩下的代码很顺利的写完了
逻辑如下：
>+ 首先，需要确认链表是否为空，空的话返回none
>+ 定义两个指针，一个是none（最后一个node指向的元素），一个是head
>+ 使用while循环，遍历post指针，在这个过程中调整方向，其中temp储存post.next的数值