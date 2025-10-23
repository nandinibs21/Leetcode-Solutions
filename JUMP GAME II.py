class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        farthest = 0
        
        # We stop at n - 2 because we don’t need to jump from the last index
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # When we reach the end of the current jump range
            if i == curr_end:
                jumps += 1
                curr_end = farthest
        
        return jumps
