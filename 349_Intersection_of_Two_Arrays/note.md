done in 5 min:

only one thing: traversal the dict:

在Python中，遍历字典（`dict`）可以通过几种不同的方法实现，取决于你想要访问的是键（key）、值（value）还是键值对（key-value pair）。

1. **traversal all the key in dict**：
   ```python
   my_dict = {'a': 1, 'b': 2, 'c': 3}
   for key in my_dict:
       print(key)

2. **all the values:**
   ```python
   my_dict = {'a': 1, 'b': 2, 'c': 3}
   for value in my_dict.values():
       print(value)

3. **key and value:**
   ```python
   my_dict = {'a': 1, 'b': 2, 'c': 3}
   for key, value in my_dict.items():
       print(key, value)
   
   note .values() and .items()

# 7.22重刷
做得很快，四五分钟做完的，思路就是两个数组都取set(), 直接check，可以看py文件