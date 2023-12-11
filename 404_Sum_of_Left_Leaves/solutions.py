# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        val=0
        if root.left and root.left.left is None and root.left.right is None:
            val=root.left.val
        leftval=self.sumOfLeftLeaves(root.left)
        rightval=self.sumOfLeftLeaves(root.right)

        return val+leftval+rightval
        
        
        
        
        