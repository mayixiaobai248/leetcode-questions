# first time
use the method of level traversal.

get the result list, and get its item result[-1][0]

#second time
one thing need to pay attation:
don't forget two if sentence:
```python
if temp.left:
    queue.append(temp.left)
if temp.right:
    queue.append(temp.right)
```
otherwise it would couse an error AttributeError: 'NoneType' object has no attribute 'val' because we put Nonetype into queue