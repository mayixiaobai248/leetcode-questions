# first time

done by assistance of https://programmercarl.com/0343.%E6%95%B4%E6%95%B0%E6%8B%86%E5%88%86.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE , write the code by myself.

the process are as follows:
>
>+ 确定dp数组和下标含义：dp[i]表示数字i可以得到的最大乘积数值
>+ 确定递推公式：这一步很难，我们需要设置一个循环 j从1开始一直到 i/2，看一下是(i-j)*j更大还是dp[i-j]*j更大，前一个是两个元素，后一个是三个元素。最后再和dp[i]进行比较，选择一个最合适的j。所以dp[i]=max(dp[i],max((i-j)*j,dp[i-j]*j))
>+ 确定如何初始化：这里我们从i=2开始初始化，dp[2]=1
>+ 确定遍历顺序，从前向后遍历
>+ 递推dp