# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        cnt=0
        temp=head
        while temp.next:
            # print(temp)
            cnt+=1
            temp=temp.next
        pos=cnt
        while pos>=(cnt//2)+1:
            head=head.next
            print(head)
            pos-=1

        return head
            
