class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_index = max(max(citations), len(citations))
        # do the traverse
        for i in range(max_index, -1, -1):
            count = 0
            for j in range(0, len(citations)):
                # two conditions of h-index
                if citations[j] >= i:
                    count = count + 1
            
                if count >= i:
                    return i
        
        return 0
