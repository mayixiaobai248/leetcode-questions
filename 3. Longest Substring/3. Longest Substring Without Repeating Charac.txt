class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxres=0
        heapq=defaultdict(int)
        window=deque()

        for i in s:
            heapq[i]=heapq[i]+1
            window.append(i)

            if heapq[i]>1:
                while heapq[i]>1:
                    temp=window.popleft()
                    heapq[temp]=heapq[temp]-1

            maxres=max(maxres,len(window))

        return maxres
