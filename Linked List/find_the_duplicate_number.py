from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Tortoise and Hare or
        # Floyd's Cycle finding algorithm
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

nums = [1, 3, 4, 2, 2]
res = Solution().findDuplicate(nums)
print("Duplicate:", res)