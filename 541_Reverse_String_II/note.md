# two pointers; string

left point to 0; 0+2k;0+4k...
right point to (left+k) always

**onething need to pay attation:**
(1) reverse the string in python:
```python
string = "Hello World"
reversed_string = string[::-1]
```
(2) round down in python
use "//" or math.floor() function

(3) In Python, if you attempt to access a range of an array (or list) that extends beyond its actual length, Python will not throw an error. Instead, it handles this request in a tolerant manner.
```python
arr = [1, 2, 3]
result = arr[0:5]
print(result)

output:[1, 2, 3]
```