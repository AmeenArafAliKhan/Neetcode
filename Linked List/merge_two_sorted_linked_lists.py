from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next
       
inp1 = [1,2,4]
inp2 = [1,3,5]

# Build a real linked list from the array: 0 -> 1 -> 2 -> 3
head1 = ListNode(inp1[0])
curr = head1
for val in inp1[1:]:
    curr.next = ListNode(val)
    curr = curr.next
head2 = ListNode(inp2[0])
curr = head2
for val in inp2[1:]:
    curr.next = ListNode(val)
    curr = curr.next

res = Solution().mergeTwoLists(head1, head2)

# Print the merged list
out = []
while res:
    out.append(res.val)
    res = res.next
print("Merged:", out)