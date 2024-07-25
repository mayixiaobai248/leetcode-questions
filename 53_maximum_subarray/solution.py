# greedy algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # greedy algorithm
        result = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count < 0:
                count = 0
        return result
