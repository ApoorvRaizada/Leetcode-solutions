class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
        # pivot = nums[right]
        # i = left - 1 
        # for j in range(left, right):
        #     if nums[j] < pivot:
        #         i += 1
        #         nums[i], nums[j] = nums[j], nums[i] # Swap smaller element forward
        #         # Move pivot to its correct final position
        #         nums[i + 1], nums[right] = nums[right], nums[i + 1]