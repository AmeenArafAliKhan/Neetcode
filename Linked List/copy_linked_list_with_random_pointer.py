import collections
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = collections.defaultdict()
        oldToCopy[None] = None
        curr = head
        while curr:
            temp = Node(curr.val)
            oldToCopy[curr] = temp
            curr = curr.next
        curr = head
        while curr:
            temp = oldToCopy[curr]
            temp.next = oldToCopy[curr.next]
            # The edge case where curr.next is None is handled by line 2
            temp.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]

# Input: [value, random_index] pairs. random_index refers to position in the array, None means no random.
inp = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

# Build the original linked list from the array
nodes = [Node(val) for val, _ in inp]
for i, (_, r) in enumerate(inp):
    nodes[i].next = nodes[i + 1] if i + 1 < len(nodes) else None
    nodes[i].random = nodes[r] if r is not None else None
head = nodes[0]

res = Solution().copyRandomList(head)

# Print the copied list as [value, random_index] pairs for easy comparison
out = []
index = {}
curr = res
i = 0
while curr:
    index[curr] = i
    curr = curr.next
    i += 1
curr = res
while curr:
    out.append([curr.val, index[curr.random] if curr.random else None])
    curr = curr.next
print("Copied list:", out)

# Verify it's a true deep copy (different nodes, same structure)
original_nodes = set()
curr = head
while curr:
    original_nodes.add(id(curr))
    curr = curr.next
deep = all(id(n) not in original_nodes for n in (res,))
print("Deep copy (no shared nodes):", deep)