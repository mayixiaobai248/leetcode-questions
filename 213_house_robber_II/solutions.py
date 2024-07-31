class Solution:
    def rob_function(self, nums: List[int]) -> int:
        dp = [0]*len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[len(nums) - 1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        sc1 = self.rob_function(nums[1:])
        sc2 = self.rob_function(nums[:-1])
        result = max(sc1, sc2)
        return result
        