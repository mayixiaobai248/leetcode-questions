class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length=len(nums)  # record the original length
        nums=nums+nums #get new array
        print(nums)
        stack=[0]
        result=[-1]*len(nums)  #2*original length

        for i in range(1,len(result)):
            while len(stack)>0 and nums[i]>nums[stack[-1]]: #situation 1  nums[stack[-1]] !!!!! mention, !!!!! mention the index
                temp=stack[-1]
                result[temp]=nums[i]
                stack.pop()
            
            stack.append(i) 
        
        final_result=result[:length]
        return final_result


        