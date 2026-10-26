#Approach: Use a dummy node to simplify the merging process. 
#Traverse both lists simultaneously and connect the smaller node to the result list.
#For the case where one list is exhausted, connect the remaining nodes of the other list.


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 or list2

        return dummy.next