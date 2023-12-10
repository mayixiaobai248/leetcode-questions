# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        path=[]
        self.traversal(root,result,path)
        return result

    def traversal(self,root,result,path):
        path.append(root.val)
        if root.left is None and root.right is None:
            result.append("->".join(map(str,path)))
        if root.left:
            self.traversal(root.left,result,path)
            path.pop()
        if root.right:
            self.traversal(root.right,result,path)
            path.pop()



        