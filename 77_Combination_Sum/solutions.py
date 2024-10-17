class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracing(candidates, target, 0, [], result)
        return result
    def backtracing(self, candidates, target, startindex, path, result):
        if sum(path) == target:
            result.append(path[:])
            return
        if sum(path) > target:
            return
        for i in range(startindex, len(candidates)):
            path.append(candidates[i])
            self.backtracing(candidates, target, i, path, result)
            path.pop()