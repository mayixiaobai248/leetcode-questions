class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if abs(target) > sum_nums :
            return 0
        if (sum_nums + target) % 2 == 1:
            return 0
        final = (sum_nums + target) // 2
        dp = [0]*(final+1)
        dp[0] = 1
        for num in nums:
            for j in range(final, num-1, -1):
                dp[j] = dp[j]+ dp[j-num]
        
        return dp[final]