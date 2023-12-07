<span style="color: red;">can do this quetions again!!!</span>

follow the mind of https://www.bilibili.com/video/BV1my4y1Z7jj/?vd_source=c267539126727892134dab0df8d3c23b and write the code by myself

**the process are as follows:**
>+ We need to maintain a monotonically increasing stack, the stack stores all the index of array.
>+ When the number temperatures[i]> top element of the stack, record the value and pop it.
>+ when < or ==, add the index into stack.

**something about syntax of stack data structure:**
>+ In python, we use list to achieve stack. **stack[-1]** is used to access the **top element of the stack**, -1 represents the last element of the list. In the context of a stack, the last element is the most recently added one, which is the top element of the stack
>+ **stack.append(item):** This method is used to add a new element to the top of the stack. This is equivalent to the 'push' operation of the stack.
>+ **stack.pop():** This method is used to remove and return the element from the top of the stack. If the stack is empty, this method will raise an IndexError exception. This is the 'pop' operation of the stack.