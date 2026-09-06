from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
       
inp = [0,1,2,3]

# Build a real linked list from the array: 0 -> 1 -> 2 -> 3
head = ListNode(inp[0])
curr = head
for val in inp[1:]:
    curr.next = ListNode(val)
    curr = curr.next

res = Solution().reverseList(head)

# Print the reversed list
out = []
while res:
    out.append(res.val)
    res = res.next
print("Reversed:", out)