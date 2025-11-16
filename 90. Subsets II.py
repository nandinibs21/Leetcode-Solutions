
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtrack(start):
            res.append(subset.copy())

            for i in range(start, len(nums)):
                # Skip duplicates at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return res
