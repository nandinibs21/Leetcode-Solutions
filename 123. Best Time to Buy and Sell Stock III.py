class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        for p in prices:
            buy1 = max(buy1, -p)          # buy first stock
            sell1 = max(sell1, buy1 + p)  # sell first stock
            buy2 = max(buy2, sell1 - p)   # buy second stock using profit from first
            sell2 = max(sell2, buy2 + p)  # sell second stock

        return sell2
