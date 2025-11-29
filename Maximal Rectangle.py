class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for r in range(rows):
            # Build histogram for this row
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # Compute largest rectangle in current histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    # Standard monotonic stack solution for "Largest Rectangle in Histogram"
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        
        # Clear remaining
        while stack:
            h = heights[stack.pop()]
            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1
            max_area = max(max_area, h * width)
        
        return max_area
