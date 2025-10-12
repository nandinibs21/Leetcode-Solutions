class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, combo, remaining):
            if remaining == 0:
                res.append(list(combo))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue
                combo.append(candidates[i])
                backtrack(i, combo, remaining - candidates[i])
                combo.pop()  # backtrack
        
        backtrack(0, [], target)
        return res
