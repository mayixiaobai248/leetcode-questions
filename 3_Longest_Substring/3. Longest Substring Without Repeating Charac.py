
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        window = deque()
        letter=defaultdict(int)

        for i in s:
            letter[i] = letter[i]+1
            window.append(i)

            if letter[i] > 1:
                while letter[i] >1:
                    window.popleft()
                    letter[i]=letter[i]-1
            
            length=max(length,len(window))
        return length