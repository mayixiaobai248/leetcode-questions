class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all_sum = sum(nums)
        if all_sum % 2 == 1:
            return False

        bagweight = int(all_sum / 2)

        dp = [[0]*(bagweight + 1) for _ in range(len(nums))]

        # initiate
        for j in range(bagweight + 1):
            if j == nums[0]:
                dp[0][j] = 1

        for i in range(1, len(nums)):
            for j in range(bagweight + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]

        return dp[len(nums) - 1][bagweight]