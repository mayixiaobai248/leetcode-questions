# first time

<font color="red">Need to do again!!!</font>
To solve the question, we need to use queue() to append and pop items in binary tree.

In addition, we need to know every layer in tree, thus we use an array and a value (size )to capture this.

For example, when we traversal the first layer, we put root in deque, and memory its size len(deque).

we need to pay attation the position of level=[] in function, it capture the subarray(numbers in each layer).

**Key Aspect - Fixed Loop Length: The crucial point here is that len(tempres) is evaluated once at the beginning of the for loop and remains constant throughout that iteration of the for loop. This means that even if new nodes (children of nodes at the current level) are added to tempres, they will not be processed in the current iteration of the for loop. They will be processed in the next iteration of the while loop, representing the next level of the tree.**

# second time
Can write all the code by myself in 10 min, but there are two things to pay attation:
>
>+ the exception need to notifiy, because you always put root into deque(), and root can be none
> ```python
>    if root is None:
>    return []
>```
>+ use deque() to store instead of list

# third time
使用递归的方法去做，更简单方便
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return 

        levels = []
        def traverse(node, level):
            if node is None:
                return 
            
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            traverse(node.left, level+1)
            traverse(node.right, level+1)

        traverse(root, 0)
        return levels
```
层序遍历嘛，首先如果是新的一层的话需要加一个[]
如果确定节点是在这一层，那么往这里面填充数值