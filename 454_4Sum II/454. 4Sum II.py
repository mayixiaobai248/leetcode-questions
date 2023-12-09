class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res=defaultdict(int)
        count=0
        for temp1 in nums1:
            for temp2 in nums2:
                res[temp1+temp2]=res[temp1+temp2]+1
        
        for temp3 in nums3:
            for temp4 in nums4:
                count=count+res[-(temp3+temp4)]
        
        return count