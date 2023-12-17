# first time

<font color=red>can do it again!!!</font>

(1) I have done this question several times, First I use brute force, and it didn't pass because of **time limit**, this process traverse the height[] by colomn.

(2) I use mono stack to solve, this process traverse the height array by row. there are 3 choice if a new number height[i] comes:
>
>+ if height[i]< height[stack[-1]]: put i into stcak
>+ if height[i]< height[stack[-1]]: pop out the old one, put i into stcak
>+ if height[i]> height[stack[-1]]: there is a groove formed, which can store rains, we need to compute them.

![picture for it](./picture%20for%20it.png)

something need to pay attention:

for the third choice, we need to put i into stack finally, because it can form another groove later.

# second time

I can write the frame by myself quickly, but some details need to pay attation, especially the third situation:
>
>+ because we need to get the left and mid, so we need to judge whether stack is [] twice.
>+ use 'while' sentence, because 'i' maybe very big and pop lots of items in stack
>+ we need to append 'i' at the end of each situation
