class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[-1]*len(nums1)
        for i in range(len(nums1)):
            tempind=nums2.index(nums1[i]) #record the index in nums2
            for j in range(tempind+1,len(nums2)):
                if nums2[j]>nums2[tempind]:
                    print(nums2[j])
                    result[i]=nums2[j]
                    break
        
        return result

# easy question, mention the location of break sentence