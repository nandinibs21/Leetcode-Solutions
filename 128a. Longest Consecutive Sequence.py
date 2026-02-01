from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for x in s:
            # Only start from sequence starts
            if x - 1 not in s:
                y = x
                while y in s:
                    y += 1
                best = max(best, y - x)

        return best
