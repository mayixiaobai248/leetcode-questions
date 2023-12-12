# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        res=self.traversal(root,targetSum-root.val)
        return res

    def traversal(self,root,count):
        if root.left is None and root.right is None:
             #leaf
            if count==0:
                return True
            else:
                return False
        if root.left:
            count=count-root.left.val
            if self.traversal(root.left,count):
                return True
            count=count+root.left.val
        if root.right:
            count=count-root.right.val
            if self.traversal(root.right,count):
                return True
            count=count+root.right.val
        return False      
        


        