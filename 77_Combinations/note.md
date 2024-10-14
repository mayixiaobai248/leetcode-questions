# first time

第一次做回溯的题目，不太会做

回溯的本质是把它们展开成一棵树，然后进行深度优先遍历

然后不断的弹出和加入元素，有固定模板

```text
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
```

详情可见https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80

对于这道题目，我的backtracking函数可以这样写：

- 终止条件：如果当前path的程度已经满足k的要求，那么存放结果，return

- for循环是选择本层中的元素，但是本层的元素并不是每次都从1开始，比如如果是2开始，本层元素就是3和4，因此需要记录一下startindex

- 处理节点就是加入path，回溯就是pop

