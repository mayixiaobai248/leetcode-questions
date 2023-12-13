# the question of sliding window and array

to solve the problem, we need to use slide window, define 2 pointers.

>+ if the sum of value in window > target, we need to record the length and move the left pointer.
>+ if the sum of value in window < target, we need to move the right pointer.
>+ for the condition to terminate, the right pointer point to the final value.