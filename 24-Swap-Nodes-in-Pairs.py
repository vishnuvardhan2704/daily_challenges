# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
            if head == None or head.next == None:
                return head

            dummy = ListNode(0, head)
            p1 = dummy
            p2 = head


            while p2 and p2.next:
                first = p2
                second = p2.next
                next_pair = second.next
                p1.next = second
                second.next = first
                first.next = next_pair
                p1 = first
                p2 = next_pair

            return dummy.next


        