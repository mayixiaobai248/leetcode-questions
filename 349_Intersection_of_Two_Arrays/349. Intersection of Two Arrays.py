class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums3=set(nums1)
        nums4=set(nums2)
        dic=defaultdict(int)
        result=[]

        for index1 in nums3:
            dic[index1]=dic[index1]+1  #get all the number from nums1
        
        for index2 in nums4:
            dic[index2]=dic[index2]+1  #get all the number from nums1

        for key,values in dic.items():
            if values>1:
                result.append(key)

        return result

# 7.22 重刷
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = []

        for i in nums1:
            if i in nums2:
                result.append(i)
        
        return result