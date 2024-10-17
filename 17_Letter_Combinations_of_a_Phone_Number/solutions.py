from typing import List

class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        result = []
        self.backtracking(digits, 0, [], result)
        return result

    def backtracking(self, digits, index, path, result):
        if len(path) == len(digits):
            result.append(''.join(path))  
            return  
        
        letters = self.letterMap[int(digits[index])]
        
        for i in range(len(letters)):
            path.append(letters[i])  
            self.backtracking(digits, index + 1, path, result) 
            path.pop()
