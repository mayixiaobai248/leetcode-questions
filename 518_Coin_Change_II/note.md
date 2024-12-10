# first time
用完全背包一次过

### 完全背包和01背包的区别
完全背包物品可以重复的放，所以写法是这样的
```python
        for i in coins:
            for j in range(weight, bagweight):
                dp[j] = dp[j] + dp[j-weight]
```
而01背包是从前往后遍历