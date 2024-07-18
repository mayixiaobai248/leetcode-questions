class Solution:
    def mindepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None:
            return self.mindepth(root.right) + 1
        if root.right is None:
            return self.mindepth(root.left) + 1
        
        return min(self.mindepth(root.left), self.mindepth(root.right)) + 1

  