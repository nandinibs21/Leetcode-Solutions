from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        min_value = min(nums)
        max_value = max(nums)

        if min_value == max_value:
            return 0

        # Ceiling division:
        # ceil((max_value - min_value) / (n - 1))
        bucket_size = max(
            1,
            (max_value - min_value + n - 2) // (n - 1)
        )

        bucket_count = (max_value - min_value) // bucket_size + 1

        bucket_min = [float("inf")] * bucket_count
        bucket_max = [float("-inf")] * bucket_count
        bucket_used = [False] * bucket_count

        for number in nums:
            bucket_index = (number - min_value) // bucket_size

            bucket_min[bucket_index] = min(
                bucket_min[bucket_index],
                number
            )
            bucket_max[bucket_index] = max(
                bucket_max[bucket_index],
                number
            )
            bucket_used[bucket_index] = True

        maximum_gap = 0
        previous_max = min_value

        for index in range(bucket_count):
            if not bucket_used[index]:
                continue

            maximum_gap = max(
                maximum_gap,
                bucket_min[index] - previous_max
            )

            previous_max = bucket_max[index]

        return maximum_gap

