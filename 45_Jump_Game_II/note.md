# 7.26第一遍

思路想出来了没有错，但是代码有点难写

每次都走能覆盖更多的那个步幅

要重新刷的

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        i = 0
        count = 0
        cover = 0

        while i <= cover:
            for i in range(i, cover + 1):
                cover = max(nums[i] + i, cover)
                if cover >= len(nums) - 1:
                    return count + 1
            count += 1

        return count
```

cover代表可以覆盖到的最大范围，在for循环执行的过程中，cover还是原来那个cover，代表这一轮次。当这层for循环结束后，重新执行while条件开始下一轮for循环，此时cover才执行最新的标准。每一个轮次，代表跳跃了一步，count++
