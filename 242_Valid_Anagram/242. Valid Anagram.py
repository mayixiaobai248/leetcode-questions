class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record=defaultdict(int)
        for i in s:
            record[i]=record[i]+1
        for i in t:
            record[i]=record[i]-1

        are_all_zeros = all(value == 0 for value in record.values())
        return are_all_zeros