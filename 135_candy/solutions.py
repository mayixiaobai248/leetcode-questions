class Solution:
    def candy(self, ratings: List[int]) -> int:
        have_candy = [1]*len(ratings)
        # traverse from front to end
        for i in range(0, len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                have_candy[i+1] = have_candy[i] + 1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                have_candy[i] = max(have_candy[i+1] + 1 , have_candy[i])

        # compute the result       
        result = 0
        for i in range(0, len(ratings)):
            result = result + have_candy[i]

        return result