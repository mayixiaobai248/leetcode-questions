# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        #find the max value in list
        max_value=max(nums)
        max_val_index=nums.index(max_value)
        root=TreeNode(max_value)

        nums_left=nums[:max_val_index]
        nums_right=nums[max_val_index+1:]

        root.left=self.constructMaximumBinaryTree(nums_left)
        root.right=self.constructMaximumBinaryTree(nums_right)

        return root