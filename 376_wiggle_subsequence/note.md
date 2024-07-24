这道题快烦死我了

首先我以为是找连续的摆荡序列，然后想着用双指针去做，但事实证明题中的意思是可以从里面删除元素，找到最长的。

然后就定义呗，也就是波峰和波谷保留，其他删除，我是这么想的：
>+ 开始定义result = 2，即首尾元素，遇到其他的波峰或者波谷result++
>+ 至于如何定义波峰或者波谷，(nums[i] - nums[i-1]) * (nums[i] - nums[i+1]) < 0
>+ 后来在测试样例的时候，发现了几个问题，对于[0, 0, 0]这种，首尾不应该都计入
>+ 然后如果很多相同的元素出现在波峰或者波谷[1, 2, 2, 2, 1]这种，没有计入

代码随想录里面是这么写的：
```python
class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums) 
        curDiff = 0  # 当前一对元素的差值
        preDiff = 0  # 前一对元素的差值
        result = 1  # 记录峰值的个数，初始为1（默认最右边的元素被视为峰值）
        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]  # 计算下一个元素与当前元素的差值
            # 如果遇到一个峰值
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1  # 峰值个数加1
                preDiff = curDiff  # 注意这里，只在摆动变化的时候更新preDiff
        return result  # 返回最长摆动子序列的长度
```