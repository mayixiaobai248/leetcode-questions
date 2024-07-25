# 01 背包问题的二维数组法

详细讲解：https://programmercarl.com/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.html#%E6%80%9D%E8%B7%AF

有n件物品和一个最多能背重量为w 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。

**使用暴力解决方法**：每一件物品其实只有两个状态，取或者不取，所以可以使用回溯法搜索出所有的情况，那么时间复杂度就是$o(2^n)$，这里的n表示物品数量。

![avatar](/0_01bag_question/picture.png)

对于这个问题，动规五部曲如下：
1. 确定dp数组和下标的含义：
>
>+ dp[i][j] 其中i表示第1-i件物品任取放到背包里，j表示背包所能承受的最大重量，d[i][j]表示物品的价值。

2. 确定递推公式
>
>+ 当第i件物品没有放到背包里：d[i][j]=d[i-1][j]
>+ 当第i件物品放到背包里:d[i][j]=d[i-1][j-weight[i]]+value[i]

3. 确定初始化
>
>+ 是一个二维数组，其中i表示物品，j表示背包，每个d[i][j]是由左上角和正上方的元素推出，初始化可以初始化第一行和第一列。

4. 确定遍历顺序
>
>+ 先遍历背包，后遍历物品，反过来也行。

```python
# 这个是自己写的
def test():
    all_value = 6
    weight = [2, 2, 3, 1, 5, 2]
    value = [2, 3, 1, 5, 4, 3]
    bagweight = 1

    dp = [[0]*(bagweight + 1) for _ in range(all_value)]

    for j in range(bagweight + 1):
        if j >= weight[0]:
            dp[0][j] = value[0]
            
    for i in range(1, all_value):
        for j in range(bagweight + 1):
            if j < weight[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-weight[i]] + value[i])
            
    return dp[all_value-1][bagweight]
  
```

在我自己写的时候出现了几个问题：
>+ 首先是dp数组的规格，因为物品是根据下标走的，可以从[0, len(value)-1]，但是对于背包容量，j是多少就是多少，所以j需要[0, bagweight]
>+ 其次开始在遍历的时候我没有写判断语句，一直报错list out of range，后来发现一个是i要从下表1开始遍历，因为i = 0已经赋值了，其次dp[i-1][j-weight[i]] 要保证是合法的，也就是说j要大于weight[i]，仔细想一下如果j小于weight[i]，那么根本装不了这件物品

# 01 背包的一维数组解法

我们发现：
```python
dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
```
其实就相当于把上一层的数据拷贝下来。因此只需要保留d[j]就可以。
```python
d[j]=max(dp[j],dp[j-weight[i]]+value[i])
```

转化为一维数组后遍历顺序要额外注意一下：
>
>+ 先遍历物品，再遍历背包 (先遍历背包的话物品只会被添加一次)
>+ 背包要倒序遍历（因为是01背包物品只能被添加一次）

<font color='red'>这一块理解的不是很到位，需要再次理解</font>

