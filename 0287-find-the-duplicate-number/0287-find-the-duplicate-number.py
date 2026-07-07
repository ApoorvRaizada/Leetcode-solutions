class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        # slow=head
        # fast=head
        # while fast!=None and fast.next!=None:
        #     slow=slow.next
        #     fast=fast.next.next

        #     if slow==fast:
        #         return slow.val