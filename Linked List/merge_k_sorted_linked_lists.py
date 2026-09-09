from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists
        return lists[0]
    def mergeLists(self, l1, l2):
        dummy = ListNode()
        node = dummy
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1 or l2:
            node.next = l1 or l2
        return dummy.next


# Input: a list of sorted arrays. Each is turned into its own linked list.
inp = [[1, 4, 5], [1, 3, 4], [2, 6]]


def build_list(vals):
    ll = ListNode(vals[0])
    curr = ll
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return ll


lists = [build_list(vals) for vals in inp]
res = Solution().mergeKLists(lists)

# Print the merged list
out = []
while res:
    out.append(res.val)
    res = res.next
print("Merged:", out)