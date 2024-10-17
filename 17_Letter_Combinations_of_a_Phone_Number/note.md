### First Time
还是用回溯方法的思路，写代码的时候有几个方面要注意一下
```python
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
```
首先是这个init函数，初始化了一个字母表
```python
        letters = self.letterMap[int(digits[index])]
```
注意再次引用字母表要加上self，并且要把char转换成int
