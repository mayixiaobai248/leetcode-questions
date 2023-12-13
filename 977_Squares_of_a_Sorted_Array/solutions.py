class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        results=[]
        for i in nums:
            results.append(i*i)
        results.sort()

        return results