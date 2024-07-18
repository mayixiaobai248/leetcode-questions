### 7.18 第一遍做出来了

思路如下(这个思路适用于977题）：

> + [a, b, c, d, e, f, g]
> + 首先定义两个变量，一个指向最左边，一个指向最右边
> + 如果left == target, 互换元素，此时right所指向的数字一定是target，left指向的不知道，right = right -1
> + 如果left != target，直接left++
> + 然后看一下临界

但是发现**似乎想复杂了**

### 这道题最好的是使用**快慢指针的方法**：



定义快慢指针

- 快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组
- 慢指针：指向更新 新数组下标的位置

```python
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index=index+1
        
        return index
```