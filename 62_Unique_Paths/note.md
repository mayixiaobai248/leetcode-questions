# first time

done by myself in 4 min, don't need to do it again

the process are as follows:

1. 确定dp数组和下标含义
>
>+ dp[i][j] 表示到达（i,j）时一共有几条路径
2. 确定递推公式
>
>+ dp[i][j]=dp[i-1][j]+dp[i][j-1]
3. 确定如何初始化
>
>+ 第一行和第一列全都是1
4. 确定遍历顺序
>
>+ 一行一行遍历，从上而下，从左向右
5. 递推dp，没有错误所以跳过