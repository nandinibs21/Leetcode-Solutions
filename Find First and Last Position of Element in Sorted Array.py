class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findLeft():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        def findRight():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        left, right = findLeft(), findRight()
        if left <= right and right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        return [-1, -1]
