class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 0
        for n in nums:
            x ^= n
        return x
