from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        curr = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

# Digits are stored in reverse order: [2,4,3] represents 342
l1 = [2, 4, 3]
l2 = [5, 6, 4]


def build_list(vals):
    ll = ListNode(vals[0])
    curr = ll
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return ll


list1 = build_list(l1)
list2 = build_list(l2)

res = Solution().addTwoNumbers(list1, list2)

# Print the sum in the same reversed-digit format (leading order)
out = []
curr = res
while curr:
    out.append(curr.val)
    curr = curr.next
print("Sum (reversed digits):", out)