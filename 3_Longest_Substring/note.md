#Sliding window question

<font color='red'> need to do again!!</font>
<font color='blue'> have done twice</font>
we use slide window to solve this question, we use heapq as a dist to record frequency of number inside the window, 

if the frequence>1,then, it is deplicate and need to change the left side of window.

**There are something need to know:**
>+ defaultdict(int), initialize the dict, all of the value is 0 (defaultdict[i]=0 is default).
>+ use deque() to mimic slide window, window=deque(), use window.append() to add new item, use window.popleft() to remove item.
>+ use while loop to change the left side of slide window, until all of items in slide window frequency<=1.
