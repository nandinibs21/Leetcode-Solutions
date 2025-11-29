class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # will store indices
        max_area = 0
        n = len(heights)

        for i in range(n):
            # If current bar is smaller, pop from stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # If stack is empty, width extends from 0 to i-1
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)

        # Clear remaining stack
        while stack:
            h = heights[stack.pop()]
            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1
            max_area = max(max_area, h * width)

        return max_area
