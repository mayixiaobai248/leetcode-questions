# first time
这是一道复杂的题目，代码随想录上的方案是通过从前向后和从后向前两次遍历来确定
- 首先是从前向后遍历，初始化数组都为1（因为每个小孩必须有糖），如果后一项比前一项大，那么更新数值为前一项+1
- 然后从后向前遍历，如果前一项比后一项大，那么比较一下自身的数值和后一项+1，取最大的值
- 最后统计结果

应该重新做一遍