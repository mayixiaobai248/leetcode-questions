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
```
notify the first return sentence, it is necessary.