it is a easy question,done it in 10 min.

**few things need to pay attation:**
>+ the order of if sentence, we need to first check, then add the number in list.
>+ the location of the global variable.
>+ calculate sum of square of each digit in a number.
 ```python 
  def sum_of_squares(n):
      return sum(int(digit)**2 for digit in str(abs(n)))
 ```
>+ (digit)**2 calculate the square
>

# 7.22 重刷第一遍
没有之前那么顺利，主要是做的时候出现了一个问题
```python
    def isHappy(self, n: int) -> bool:
        record = []
        while n not in record:
            # record.append(n)
            sumval = 0
            str_num = str(n)
            for i in str_num:
                sumval = sumval + int(i)**2
            if sumval == 1:
                return True
            else:
            # there
                record.append(sumval)
                n = sumval
        
        return False
```
record.append()语句放在哪，开始的时候放在there的位置，发现会有错误，想了一下原因是第一次原始的value没有放在record里面，调整逻辑放在上面，运行是对的。