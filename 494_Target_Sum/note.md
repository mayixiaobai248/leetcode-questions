# first time
这道题得再做一遍，因为最开始想的是能不能凑出来，后来反应过来问的是方法数，所以我们dp数组代表的是方法数而不是价值
按照递归三部曲来走，
1. dp[i][j]代表前i个数字，和为j的方法数
2. dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]] 因为每一个单元，要不然就是选取这个数dp[i-1][j-nums[i]]，要不然就是不选这个数dp[i-1][j] 
3. 初始化，dp[0][num[0]] = 1（对于第一行）， dp[0[j]] =1，初始化第一列
4. 遍历顺序，先遍历数字，再遍历和

在一维 DP 中，dp[j] 的含义是：在当前状态下，选取若干个物品，能否凑出和为j的方案数

## 求解有几种方法问题的套路
确定dp数组以及下标的含义
dp[j] 表示：填满j（包括j）这么大容积的包，有dp[j]种方法

确定递推公式
dp[j] += dp[j - nums[i]]

注意：求装满背包有几种方法类似的题目，递推公式基本都是这样的。

dp数组如何初始化
dp[0] 初始化为1 ，dp[j]其他下标对应的数值应该初始化为0。

确定遍历顺序
01背包问题一维dp的遍历，nums放在外循环，target在内循环，且内循环倒序。