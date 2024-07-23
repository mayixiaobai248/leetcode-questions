class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        # iterate from the largest index
        index = len(s) - 1
        result = 0
        for greed in reversed(g):
            if index >= 0 and greed <= s[index]:
                index -= 1
                result += 1
        return result