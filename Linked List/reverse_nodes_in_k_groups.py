from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: # Means it has reached None
                break
            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


head = [1, 2, 3, 4, 5]
k = 2

# Build a real linked list from the array: 1 -> 2 -> 3 -> 4 -> 5
ll = ListNode(head[0])
curr = ll
for val in head[1:]:
    curr.next = ListNode(val)
    curr = curr.next

res = Solution().reverseKGroup(ll, k)

# Print the resulting list
out = []
while res:
    out.append(res.val)
    res = res.next
print("Reversed in groups of", k, ":", out)