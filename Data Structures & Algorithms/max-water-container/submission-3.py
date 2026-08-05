class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right= len(heights)-1
        widht =0
        water=0
        maxwater=0
        while left < right:
            widht=right-left
            water=widht*min(heights[left],heights[right])
            if water>maxwater:
                maxwater=water
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
                
        return maxwater

        