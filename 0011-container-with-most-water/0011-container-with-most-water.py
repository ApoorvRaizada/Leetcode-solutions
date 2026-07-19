class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right,maxarea=0,n-1,0
        while left<right:
            width=right-left
            currarea=width*min(heights[left],heights[right])
            maxarea= max(currarea,maxarea)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxarea
        