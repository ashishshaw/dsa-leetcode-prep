#Approach: First, we create a dummy node that points to the head of the linked list. We then use two pointers, slow and fast, 
# both initialized to the dummy node. We move the fast pointer n + 1 steps ahead, so that there is a gap of n nodes between the slow and fast pointers. 
# Then, we move both pointers together until the fast pointer reaches the end of the list. 
# At this point, the slow pointer will be just before the node we want to remove. 
# We adjust the next pointer of the slow node to skip the nth node from the end.

# head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # Keep n nodes between fast and slow
        for _ in range(n + 1):
            fast = fast.next

        # Move together
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove nth node from the end
        slow.next = slow.next.next

        return dummy.next