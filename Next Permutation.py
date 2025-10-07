class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
        
        # Step 1: find the first decreasing element from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: if found, find element just larger than nums[i]
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: reverse the tail part
        nums[i + 1:] = reversed(nums[i + 1:])
