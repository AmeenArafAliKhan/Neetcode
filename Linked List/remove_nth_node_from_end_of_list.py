from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

head = [1, 2, 3, 4, 5]
n = 2

# Build a real linked list from the array: 1 -> 2 -> 3 -> 4 -> 5
ll = ListNode(head[0])
curr = ll
for val in head[1:]:
    curr.next = ListNode(val)
    curr = curr.next

res = Solution().removeNthFromEnd(ll, n)

# Print the resulting list
out = []
while res:
    out.append(res.val)
    res = res.next
print("After removing nth from end:", out)