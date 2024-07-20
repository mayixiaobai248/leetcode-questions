class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        results=[]
        for i in nums:
            results.append(i*i)
        results.sort()

        return results
    
# 双指针法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointers
        left, right = 0, len(nums) - 1
        results = [0]*len(nums)
        index = len(nums) - 1
        while(index >= 0):
            if nums[left]**2 < nums[right]**2:
                results[index] = nums[right]**2
                right = right -1
            else:
                results[index] = nums[left]**2
                left = left + 1
            index = index -1
        
        return results