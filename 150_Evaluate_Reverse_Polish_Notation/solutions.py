class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for item in tokens:
            if item=='+':
                temp1=stack.pop()
                temp2=stack.pop() # the fronter one
                temp3=temp1+temp2
                stack.append(temp3)
            elif item=='-':
                temp1=stack.pop()
                temp2=stack.pop() # the fronter one
                temp3=temp2-temp1
                stack.append(temp3)
            elif item=='*':
                temp1=stack.pop()
                temp2=stack.pop() # the fronter one
                temp3=temp1*temp2
                stack.append(temp3)
            elif item=='/':
                temp1=stack.pop()
                temp2=stack.pop() # the fronter one
                temp3=int(temp2/temp1)
                stack.append(temp3)
            else:
                stack.append(int(item))
            
        return stack[-1]

        