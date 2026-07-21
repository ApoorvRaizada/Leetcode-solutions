class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water
        # leftwall=0
        # rightwall=height[2]
        # mid=height[1]
        # for i in range(len(height)):
        #     water[i]=min(leftwall, rightwall) - height[i]
        #     leftwall=rightwall
        #     rightwall+=2
        #     mid+=2
        # return water
        