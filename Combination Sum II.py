class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates easily
        
        def backtrack(start, comb, remaining):
            if remaining == 0:
                res.append(list(comb))
                return
            if remaining < 0:
                return
            
            prev = -1
            for i in range(start, len(candidates)):
                # Skip duplicate numbers in the same recursive level
                if candidates[i] == prev:
                    continue
                if candidates[i] > remaining:
                    break
                
                comb.append(candidates[i])
                backtrack(i + 1, comb, remaining - candidates[i])
                comb.pop()
                prev = candidates[i]
        
        backtrack(0, [], target)
        return res
