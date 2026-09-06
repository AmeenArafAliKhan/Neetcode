class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pos = {}
        for i in range(len(nums)):
            temp = target -  nums[i]
            if nums[i] in pos:
                return [pos[nums[i]], i]
            pos[temp] = i
        return
    
res = Solution()
print(res.twoSum(nums = [5,5], target = 10))