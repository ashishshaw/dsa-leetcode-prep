#Approach: Floyd's Cycle Detection Algorithm (Tortoise and Hare)
#First, we initialize two pointers, slow and fast, both pointing to the head of the linked list. 
# The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. 
# If there is a cycle in the linked list, the fast pointer will eventually meet the slow pointer. 
# If the fast pointer reaches the end of the list (i.e., encounters a null reference), then there is no cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                return True
            
        return False



