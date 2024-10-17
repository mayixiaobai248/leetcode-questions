class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtracing(k, n, 1, [], result)
        return result
    def backtracing(self, k, n, startindex, path, result):
        if len(path) == k and sum(path) == n:
            # still need to pay attention path[:]
            result.append(path[:])
            return
        if len(path) == k and sum(path) != n:
            return
        
        for i in range(startindex, 10):
            path.append(i)
            self.backtracing(k, n, i+1, path, result)
            path.pop()