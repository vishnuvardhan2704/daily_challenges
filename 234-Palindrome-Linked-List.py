class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle using fast/slow pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half starting at 'slow'
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Compare first half and reversed second half
        left = head
        right = prev  # Head of the reversed second half
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True