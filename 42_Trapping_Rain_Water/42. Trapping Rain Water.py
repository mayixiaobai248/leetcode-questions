class Solution:
    def trap(self, height: List[int]) -> int:

#brute force
        # sumres=0
        # for i in range(len(height)):
        #     if i==0 and i==len(height)-1:
        #         continue
            
        #     left=height[i]
        #     right=height[i]
        #     ###需要寻找列两侧最高的柱子
        #     for j in range(i+1,len(height)):
        #         if height[j]>right:
        #             right=height[j]
        #             # break
            
        #     for k in range(i-1,-1,-1):
        #         if height[k]>left:
        #             left=height[k]
        #             # break   
        #     if (min(left,right)-height[i])>0:
        #         sumres=sumres+ min(left,right)-height[i]

        # return sumres   

# by mono stack
        sumres=0  
        stack=[0]
        for i in range(1,len(height)):
            if stack!=[] and height[i]<height[stack[-1]]:
                stack.append(i)
            if stack!=[] and height[i]==height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack!=[] and height[i]>height[stack[-1]]:
                    mid=stack[-1]
                    stack.pop()
                    if stack!=[]:
                        left=stack[-1]
                        right=i
                        sumres=sumres+(min(height[left],height[right])-height[mid])*(right-left-1)
                stack.append(i)
        
        return sumres