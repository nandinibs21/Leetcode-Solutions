from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                # Minimum is at mid or in the left half.
                right = mid

            elif nums[mid] > nums[right]:
                # Minimum must be in the right half.
                left = mid + 1

            else:
                # nums[mid] == nums[right].
                # Removing nums[right] cannot remove the only minimum,
                # because nums[mid] has the same value.
                right -= 1

        return nums[left]
