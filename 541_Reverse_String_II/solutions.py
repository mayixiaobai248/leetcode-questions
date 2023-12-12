class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left=0
        while left<len(s):
            right=left+k
            s=s[:left]+s[left:right][::-1]+s[right:]
            left=left+2*k
        
        return s