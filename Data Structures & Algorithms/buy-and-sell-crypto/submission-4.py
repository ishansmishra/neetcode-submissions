class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        mx=0
        for r in range(len(prices)):
            mx=max(prices[r]-prices[l],mx)
            if prices[r]-prices[l]<0:
                l=r
        return mx