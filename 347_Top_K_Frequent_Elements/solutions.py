from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictory=defaultdict(int)
        for i in nums:
            dictory[i]=dictory[i]+1
        
        heap=[]
        for key,value in dictory.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)

        result=[0]*k
        for i in range(k-1,-1,-1):
            result[i]=heapq.heappop(heap)[1]
        
        return result