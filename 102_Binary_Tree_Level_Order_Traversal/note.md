To solve the question, we need to use queue() to append and pop items in binary tree.

In addition, we need to know every layer in tree, thus we use an array and a value (size )to capture this.

For example, when we traversal the first layer, we put root in deque, and memory its size len(deque).

we need to pay attation the position of level=[] in function, it capture the subarray(numbers in each layer).
