class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracing(n, k, 1, [], result)
        return result
    def backtracing(self, n, k, startindex, path, result):
        if len(path) == k:
            result.append(path[:])
        for i in range(startindex, n+1):
            path.append(i)
            self.backtracing(n, k, i+1, path, result)
            path.pop()