class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtracing(candidates, target, 0, [], result)
        return result
    def backtracing(self, candidates, target, startindex, path, result):
        if sum(path) == target:
            result.append(path[:])
            return
        if sum(path) > target:
            return
        for i in range(startindex, len(candidates)):
            if i > startindex and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.backtracing(candidates, target, i+1, path, result)
            path.pop()
        