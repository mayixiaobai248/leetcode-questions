use a dict to record the change of value while loop.

**there is one thing need to pay attation:**
>+ (1) to check whether all values in dict are==0:
>+ my_dict = {'a': 0, 'b': 0, 'c': 0}  # 示例字典
   ```are_all_zeros = all(value == 0 for value in my_dict.values())```
>
>+ (2) ord("a") can obtain the ASCII of letter a 
