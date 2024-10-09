# first time

<font color="red">Need to do again!!!</font>
这道题目也使用递归方法，关键是比较左子树的外侧和右子树的外侧，左子树的内侧和右子树的内侧，如果都相同，那么就是对称的。

然后递归函数是这么写：
- 首先判断这两个节点是否相等 （是否为空， 数值是否一样）
- 如果没问题的话就去判断它的子树，注意是左子树的左节点和右子树的右节点，左子树的右节点和右子树的左节点

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left, root.right)

    def compare(self, node1, node2):
        # the situation of one subtree is none
        if node1 is None and node2 is None:
            return True
        elif node1 is not None and node2 is None:
            return False
        elif node1 is None and node2 is not None:
            return False   
        # the situation of value are same or different
        elif node1.val != node2.val:
            return False
        
        #only if two vales are same, we process their child
        leftval = self.compare(node1.left, node2.right)
        rightval = self.compare(node1.right, node2.left)
        issame = leftval and rightval
        return issame
```
