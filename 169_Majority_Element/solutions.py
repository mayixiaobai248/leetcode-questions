class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] = count[num] + 1
        
        for key, value in count.items():
            if value > len(nums)//2:
                return key