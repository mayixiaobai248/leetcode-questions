from collections import deque


class Myque:
        def __init__(self):
            self.queue=deque()
        
        def pop_item(self,value):
            if self.queue and self.queue[0]==value:
                self.queue.popleft()
        
        def push_item(self,value):
            while self.queue and value>self.queue[-1]:
                self.queue.pop()
            self.queue.append(value)
        
        def front_item(self):
            return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=Myque()
        result=[]
        for i in range(k):
            queue.push_item(nums[i])
        result.append(queue.front_item())
        for i in range(k,len(nums)):
            queue.pop_item(nums[i-k])
            queue.push_item(nums[i])
            result.append(queue.front_item())

        return result
        

        