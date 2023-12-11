<font color="red">Need to do again!!!</font>
To solve the question, we need to use queue() to append and pop items in binary tree.

In addition, we need to know every layer in tree, thus we use an array and a value (size )to capture this.

For example, when we traversal the first layer, we put root in deque, and memory its size len(deque).

we need to pay attation the position of level=[] in function, it capture the subarray(numbers in each layer).

**Key Aspect - Fixed Loop Length: The crucial point here is that len(tempres) is evaluated once at the beginning of the for loop and remains constant throughout that iteration of the for loop. This means that even if new nodes (children of nodes at the current level) are added to tempres, they will not be processed in the current iteration of the for loop. They will be processed in the next iteration of the while loop, representing the next level of the tree.**