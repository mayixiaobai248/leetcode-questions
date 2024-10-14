# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.countHeight(root) != -1
    def countHeight(self, root):
        if root is None:
            return 0
        left = self.countHeight(root.left)
        right = self.countHeight(root.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        else:
            return max(left, right)+1

        