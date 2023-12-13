class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window
        left,right=0,0
        sum=0
        min_len=float('inf')

        for right in range(len(nums)):
            sum=sum+nums[right]
            while sum>=target:
                min_len=min(min_len,right-left+1)
                sum=sum-nums[left]
                #pay attation to the order of this sentence and the following one
                left=left+1

        if min_len==float('inf'):
            return 0
        return min_len