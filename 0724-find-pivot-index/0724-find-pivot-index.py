class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        suffix[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] =suffix[i+1] + nums[i]
        for i in range(n):
            left=0 if i==0 else prefix[i-1]
            right=0 if i==n-1 else suffix[i+1]
            if right==left:
                return i
        return -1

