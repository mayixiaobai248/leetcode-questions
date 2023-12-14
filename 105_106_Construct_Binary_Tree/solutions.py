###105 preorder and inorder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        value=preorder[0]
        root=TreeNode(value) #the first value of preorder is root

        midvalue=inorder.index(root.val)

        left_in=inorder[:midvalue]
        right_in=inorder[midvalue+1:]

        length=len(left_in)
        left_pre=preorder[1:length+1]
        right_pre=preorder[length+1:]

        root.left=self.buildTree(left_pre,left_in)
        root.right=self.buildTree(right_pre,right_in)

        return root
        

###106 inorder and postorder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        value = postorder[-1]       
        root=TreeNode(value)   #the last value of postorder array is root val
        left_inorder=[]
        right_inorder=[]
        #find root.val in inorder list
        for i in range(len(inorder)):
            if inorder[i]==root.val:
                left_inorder=inorder[:i]
                right_inorder=inorder[i+1:]


        left_post=[]
        right_post=[]
        #split postorder list:
        length=len(left_inorder)
        left_post=postorder[:length]
        right_post=postorder[length:len(postorder)-1]

        root.left=self.buildTree(left_inorder,left_post)
        root.right=self.buildTree(right_inorder,right_post)

        return root
        

        