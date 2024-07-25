# 二维数组版
def test_2_wei_bag_problem1(weight, value, bagweight):
    #定义二维数组
    dp=([0]*len(bagweight+1) for _ in range(len(weight)))
    for temp in len(weight):#背包重量为0
        dp[temp][0]=0
    for temp in len(bagweight+1): #temp is the value
        if temp>weight[0]:
            dp[0][temp]=value[0]
        else:
            dp[0][temp]=0
    
    for i in range(1,len(weight)):
        for j in range(1,bagweight+1):
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
    
    return dp[len(weight)-1][bagweight]

# 这个是自己写的
def test():
    all_value = 6
    weight = [2, 2, 3, 1, 5, 2]
    value = [2, 3, 1, 5, 4, 3]
    bagweight = 1

    dp = [[0]*(bagweight + 1) for _ in range(all_value)]

    for j in range(bagweight + 1):
        if j >= weight[0]:
            dp[0][j] = value[0]
            
    for i in range(1, all_value):
        for j in range(bagweight + 1):
            if j < weight[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-weight[i]] + value[i])
            
    return dp[all_value-1][bagweight]
  

# 一维数组版
def test_1_wei_bag_problem1(weight, value, bagweight):
    #定义二维数组
    dp=[0]*len(bagweight+1)
    dp[0]=0
    
    for i in range(1,len(weight)):
        for j in range(bagweight,weight[i]-1,-1):
            dp[i][j]=max(dp[j],dp[j-weight[i]]+value[i])
    
    return dp[bagweight]




if __name__ == "__main__":

    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4
    result = test()
    print(result)