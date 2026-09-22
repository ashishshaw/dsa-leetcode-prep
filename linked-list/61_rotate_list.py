#First, we find the length of the linked list and the tail node.
# Then, we calculate the effective rotation steps by taking k modulo the length.
# If the effective steps are 0, no rotation is needed.
# Otherwise, we connect the tail to the head to form a circular list.
# We then move the new tail pointer to the position just before the new head.
# Finally, we break the circle and return the new head.

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k == 0 or (not head.next):
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        
        k = k%length
        if k==0:
            return head
        
        tail.next = head

        steps = length - k
        new_tail = head


        for _ in range(steps-1):
            new_tail = new_tail.next
        
        new_head = new_tail.next

        new_tail.next = None
        return new_head