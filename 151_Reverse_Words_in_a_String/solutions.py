class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        left=0
        right=len(word)-1
        while left<right:
            word[left],word[right]=word[right],word[left]
            left=left+1
            right=right-1

        result=" ".join(word)
        return result