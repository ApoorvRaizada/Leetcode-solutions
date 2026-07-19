class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = 0

        while left < right:

            while left < right and nums[left] != 0:
                left += 1

            while left < right and nums[right] == 0:
                right -= 1

            if left < right:
                ans += 1
                left += 1
                right -= 1

        return ans
        # n=len(nums)
        # count=0
        # left=nums[0]
        # right=n-1
        # for i in range(n):
        #     if left!=0 and right!=0:
        #         left+=1
        #         right-=1
        #     elif left==0 and right!=0:
        #         left,right=right,left
        #         left+=1
        #         right-=1
        #         count+=1
        #     elif left!=0 and right==0:
        #         left+=1
        #         right-=1
        # return count


