from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(list)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        res = sorted(count.items(), key = lambda x:x[1], reverse = True)
        print(res)
        return ([t[0] for t in res[:k]])
    


res = Solution()
print(res.topKFrequent(nums = [7,7], k = 1))