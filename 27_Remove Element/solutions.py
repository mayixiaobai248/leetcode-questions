class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index=index+1
        
        return index

# 另一个更复杂的方法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        while (left <= right):
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right = right -1
            else:
                left = left +1
            
        return (right + 1)