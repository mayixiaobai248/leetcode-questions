# 更改前
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_weight = sum(stones)
        target = int(sum_weight / 2)

        dp = [[0]*(target+1) for _ in range(len(stones))]

        for j in range(target+1):
            dp[0][j] = stones[0] if abs(j - stones[0]) < j else 0

        for i in range(len(stones)):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j] if abs(target - dp[i-1][j]) < abs(dp[i-1][j-stones[i]]+stones[i] - target) else dp[i-1][j-stones[i]]+stones[i]

        half_weight = dp[len(stones)-1][target]
        result = abs((sum_weight - half_weight) - half_weight)
        return result


# 更改后
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_weight = sum(stones)
        target = sum_weight // 2

        dp = [[0] * (target + 1) for _ in range(len(stones))]

        for j in range(target + 1):
            dp[0][j] = stones[0] if j >= stones[0] else 0

        for i in range(1, len(stones)):
            for j in range(target + 1):
                if j >= stones[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]] + stones[i])
                else:
                    dp[i][j] = dp[i-1][j]

        half_weight = dp[len(stones) - 1][target]
        result = sum_weight - 2 * half_weight
        return result