## First Time

这个题目的逻辑和combination sum基本一样，除了这道题不允许重复元素，除此之外，我们需要在result数组去重：

- 首先是sort整个数组，因为返回的元素是有顺序的

- 其次是for循环里的这个语句，如果有重复元素跳过（横向遍历树的时候，所以在for循环下面）

  ```python
     if i > startindex and candidates[i] == candidates[i - 1]:
         continue
  ```
- 最后是用i+1作为backtracking的startindex