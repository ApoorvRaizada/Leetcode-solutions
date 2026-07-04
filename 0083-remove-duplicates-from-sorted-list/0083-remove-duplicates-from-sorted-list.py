# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr and curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head
        # curr=head
        # l=0
        # while curr!=None:
        #     curr=curr.next
        #     l+=1
        # curr=head
        # for i in range(l):
        #     if curr!=curr.next:
        #         curr.next=curr.next.next
        #     return head
        