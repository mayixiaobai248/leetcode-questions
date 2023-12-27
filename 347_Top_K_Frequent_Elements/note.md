# first time
 done by assistance of https://programmercarl.com/0347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

 <font color='red'>need to do it again!!</font>

 用了大顶堆和小顶堆--适用于返回前k个最大元素或者前k个最小元素。

 the process are as follows:
 >
 >+ use dictory or map to record all the keys and frequency of nums
 >+ sort the frequency and find the top k frequent elements use Min Heap.

 (这里有个问题，为什么用小顶堆，堆本质上是用过二叉树实现的，大顶堆根节点比左右孩子都大，小顶堆根节点比左右孩子都小。因为我们需要不断pop出元素，pop的是堆的根节点，所以才用小顶堆，这样剩下来的元素就是top k个最大的)

还有一些关于堆和dict的语法问题：

**1. 遍历dict：**

use items() 遍历key和value
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)
```

use keys() 遍历key
```python
for key in my_dict.keys():
    print(key)
```

use values() 遍历values
```python
for value in my_dict.values():
    print(value)
```

**2. 小顶堆相关**
>
>+ 特点：堆顶（即堆的第一个元素）是最小元素。
>+ 创建：使用 heapq.heapify(list) 将列表转换成小顶堆。
>+ 插入元素：使用 heapq.heappush(heap, item) 将元素添加到堆中。
>+ 弹出最小元素：使用 heapq.heappop(heap) 移除并返回堆顶元素（最小元素）。
>+ 查看堆顶元素：直接访问堆的第一个元素 heap[0]。
>+ 堆替换：heapq.heapreplace(heap, item) 弹出并返回堆顶元素，然后将新元素添加到堆中。

在Python中使用heapq模块处理像[(1, 'a'), (2, 'b'), (3, 'c')]这样的列表时，小顶堆（Min Heap）的排序是基于列表中每个元组的第一个元素。

如果pri_que是这样的一个堆：[(1, 'a'), (2, 'b'), (3, 'c')]，那么执行heapq.heappop(pri_que)[1]将会返回'a'，因为'a'与最小优先级1关联。同时，元组(1, 'a')将从堆中移除。