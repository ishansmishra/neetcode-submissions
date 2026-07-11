class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        sm=0
        while r>=l:
            sm=max(sm,min(heights[r],heights[l])*(r-l))
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return sm