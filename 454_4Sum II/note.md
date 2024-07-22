# first time
To solve this question, we need to use dict. **The process are as follows:**

(1) traverse nums1 and nums2, record all of the key nums1[i]+ nums2[j],and their frequency of appear

(2) traverse nums3 and nums4, and check whether the counterpart value is appeared in dict(),get the value.

Nothing need to pay attation, time n^2

# second time 
done in 15 min

# 7.22重刷第一遍
就是2sum的变体，可以比较快的做出来。在10分钟内做出来的，但是在做当中，又一次提交出了问题，当时代码是这么写的

```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record = defaultdict(int)
        result = 0
        for temp1 in nums1:
            for temp2 in nums2:
                # record[temp1+temp2] = 1
                record[temp1+temp2] += 1
        
        for temp3 in nums3:
            for temp4 in nums4:
                if -(temp3+temp4) in record:
                    # result += 1
                    result += record[-(temp3+temp4)]

        return result  
```

主要是赋值语句有问题，最开始想的是出现的数值直接做一个标记即可，但是想到他可能出现两遍三遍... 那么result应该增加多次而非一次，# 标记的是错误的，下面写的是正确的。