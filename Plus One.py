class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            digits[i] = 0
        
        # if all digits are 9, e.g. [9,9,9]
        return [1] + digits
