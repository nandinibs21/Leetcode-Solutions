class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # First appearance: add to ones
            # Second appearance: move to twos
            # Third appearance: remove from both
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones
