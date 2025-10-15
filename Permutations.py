class Solution:
    def permute(self, nums):
        res = []
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()  # backtrack
        
        backtrack([])
        return res
