class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False
    
res = Solution()
print(res.hasDuplicate([1,2,3,3]))