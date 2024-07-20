### 暴力解法可以done in 1 min:

**onething about sort the list:**
(1). list.sort(key=None, reverse=False), where key is a function that specifies a sorting criteria, and reverse is a boolean indicating whether the list should be sorted in descending order (by default, it is False, which means the list is **sorted in ascending order**).

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
```
(2). 
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
```

### 或者可以使用双指针法

left指针指向最左边的元素， right指针指向最右边的元素，两者相比较再移动。