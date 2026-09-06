from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
       
head = [1, 2, 3, 4]
index = 1

# Build a real linked list from the array: 1 -> 2 -> 3 -> 4
ll = ListNode(head[0])
curr = ll
for val in head[1:]:
    curr.next = ListNode(val)
    curr = curr.next

# Create a cycle: link the tail back to the node at `index`
if index >= 0:
    cycle_node = ll
    for _ in range(index):
        cycle_node = cycle_node.next
    curr.next = cycle_node

res = Solution().hasCycle(ll)
print("Has cycle:", res)