# first time

done in 10 min, with twice submission, don't need to do it again.

first I want to mention **how to define 2-dimentsion array**:
```python
m=len(obstacleGrid) 
n=len(obstacleGrid[0])
dp=[[0]*n for _ in range(m)]
```
其中m表示行数，n表示列数

这个问题和前一个问题本质上的区别在于初始化，在这个问题中，如果是个障碍物，那么dp[i][j]初始化为0，表示此路不通。

注意dp[i][0]=1和dp[0][j]=1的初始化，第一次没有通过是这个细节的问题。
