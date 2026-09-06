from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Three main steps:
        1. Find mid point using slow and fast
        2. Reverse the second half
        3. Merge both lists
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
       
inp = [0,1,2,3]

# Build a real linked list from the array: 0 -> 1 -> 2 -> 3
head = ListNode(inp[0])
curr = head
for val in inp[1:]:
    curr.next = ListNode(val)
    curr = curr.next

Solution().reorderList(head)

# Print the reordered list
out = []
curr = head
while curr:
    out.append(curr.val)
    curr = curr.next
print("Reordered:", out)