class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()

        for index,value in enumerate(nums):
            if (target-value) in record:
                return[index,record[target-value]]
            else:
                record[value]=index

        return []