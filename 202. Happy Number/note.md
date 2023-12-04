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