# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result=self.traversal(root)
        return result[-1][0]

    def traversal(self, root):
        if root==None:
            return []
        tempres=deque()
        tempres.append(root)
        result=[]

        while tempres:
            level=[] #!!!!!!
            for i in range(len(tempres)):  #get the length for every layer
              
                tem_val=tempres.popleft()
                level.append(tem_val.val)
                if tem_val.left:
                    tempres.append(tem_val.left)
                if tem_val.right:
                    tempres.append(tem_val.right)
            if level:
                result.append(level)
        
        return result