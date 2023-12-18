class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        res=[]
        tempnum=n
        while 1:
            tempnum=sum(int(digit)**2 for digit in str(tempnum))
            if tempnum==1:
                return True
            if tempnum in res:
                return False  
            if tempnum not in res:
                res.append(tempnum)