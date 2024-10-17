## First time

独立使用回溯方法做的第一道题，下面我分别说一下思路，以及注意点

#### 思路

继续使用组合那道题目的理解方式，构造树，树的深度就是k

但是终止条件有一些变化，我们希望符合要求的才能加入result，不符合要求但又达到深度的就直接舍弃，所以终止条件这一块的代码是这样的：

```python
        if len(path) == k and sum(path) == n:
            # still need to pay attention path[:]
            result.append(path[:])
            return
        if len(path) == k and sum(path) != n:
            return
```
其他的思路基本上是一样的

#### 注意点
这道题目第一遍提交的时候没有通过，里面显示所有的数都是空的，后来发现是这个原因：
```python
result.append(path[:])
```

[:]的作用是浅拷贝，在这里我们需要的是浅拷贝而不是path的引用，所以差别很大
