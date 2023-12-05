class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res_dict=defaultdict(int)
        for temp1 in magazine: #traverse magezine, and record the frequency of letter
            res_dict[temp1]=res_dict[temp1]+1
        
        for temp2 in ransomNote:
            res_dict[temp2]=res_dict[temp2]-1
        #when the letter appear, the value--

        for value in res_dict.values():
            if value<0:
                return False
        
        return True