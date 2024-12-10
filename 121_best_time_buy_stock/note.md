# 8.1 第一次刷
这是一个系列，我直接去看代码随想录的讲解了。第一题是只能买卖一次

下面是动态规划五步曲，dp需要表示两种状态
>+ dp[i][0] 表示在i的时候持有股票，手头剩余的钱。dp[i][1]表示在i的时候不持有股票，手里剩余的钱。这里说的是“持有”，“持有”不代表就是当天“买入”！也有可能是昨天就买入了，今天保持持有的状态
>+ dp[i][0]由两种状态推导而来，首先i-1天的时候也持有这只股票，那么就是dp[i-1][0]，如果i-1天没有持有股票，股票是第i天买的，因为只能买入一次，那么就是-price[i]（相当于赊账买的）两者取最大值就是手头最多剩余多少钱。对于dp[i][1]也由两种状态推导而来，i-1天的时候没有持有这只股票，那么就是dp[i-1][1]，如果i-1天持有股票，是第i天卖了，那么就是dp[i-1][0]+price[i]
>+ 初始化，因为是依赖于i-1，只需要初始化dp[0][0]和dp[0][1]。dp[0][0] = -price[0], dp[0][1] = 0
>+ 遍历顺序，从前往后，一直到dp[len(price) - 1], 输出dp[len(price) - 1][1]

## 第二次
在面试高频150题中，因为很久不碰动态规划，所以用贪心算法做的。就是对于整个price数组进行了遍历，左侧取最小值，然后每次减去最小值，记录最大值。