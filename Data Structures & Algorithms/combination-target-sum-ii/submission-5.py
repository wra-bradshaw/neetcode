class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res: list[list[int]] = []
        subset: list[int] = []

        candidates = sorted(candidates)

        def dfs(i: int, current_target: int):
            if current_target == 0:
                res.append(subset.copy())
                return
            
            for next_idx in range(i, len(candidates)):
                if candidates[next_idx] > current_target:
                    break
                
                if next_idx > i and candidates[next_idx] == candidates[next_idx - 1]:
                    continue
                
                subset.append(candidates[next_idx])
                dfs(next_idx + 1, current_target-candidates[next_idx])
                subset.pop()

        dfs(0, target)
        return res