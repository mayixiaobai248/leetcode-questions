class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[0]
        for i in range(1,len(temperatures)):
            while len(stack)!=0 and temperatures[i]>temperatures[stack[-1]]:
                temp=stack.pop()
                result[temp]=i-temp
            stack.append(i)
        
        return result