use a dict to record the change of value while loop.

**there is one thing need to pay attation:**
>+ (1) to check whether all values in dict are==0:
```python
my_dict = {'a': 0, 'b': 0, 'c': 0}  # 示例字典
are_all_zeros = all(value == 0 for value in my_dict.values())
```
>+ (2) ord("a") can obtain the ASCII of letter a 
>

# 7.22日二刷
这道题很简单，可以很快的做出来，需要注意的是两个定义方式
>+ 定义defaultdict： record = defaultdict(int)
>+ all()的含义： 是 Python 内置的一个函数，用于判断可迭代对象中的所有元素是否都为真（或满足特定条件）。如果所有元素都为真，则返回 True，否则返回 False。
>+ 因此可以判断 iszero = all(value == 0 for value in record.values())
