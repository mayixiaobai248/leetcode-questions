# 8.1 重刷第一遍

反转二叉树，我主要通过递归法去做，只需要翻转该节点的left child和right child即可。

需要注意，这个只能用前序遍历和后序遍历去做。中序遍历需要考虑一种情况，就是重复翻转

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root        
```