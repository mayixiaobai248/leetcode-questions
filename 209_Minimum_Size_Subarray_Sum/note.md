# first time
the question of sliding window and array

to solve the problem, we need to use slide window, define 2 pointers.

>+ if the sum of value in window > target, we need to record the length and move the left pointer.
>+ if the sum of value in window < target, we need to move the right pointer.
>+ for the condition to terminate, the right pointer point to the final value.
>+ for the max value, define "float('inf')"

# second time

don't need to do another time, just one thing:
```python
        if minlen==float('inf'):
            return 0
        else:
            return minlen
            
       # or
       return minlen if minlen != float('inf') else 0
```
notify the first return sentence, it is necessary.

# 7.20日重刷第一遍

想到用滑动窗口的方法去做这道题， 出问题的点主要是在更新长度以及left -- 的顺序，但是很容易debug，因为离正确答案总是差一