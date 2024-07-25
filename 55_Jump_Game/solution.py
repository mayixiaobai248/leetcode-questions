class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_range = 0
        for index in range(len(nums)):
            if index > final_range:
                return False
            final_range = max(final_range, index + nums[index])

        return True