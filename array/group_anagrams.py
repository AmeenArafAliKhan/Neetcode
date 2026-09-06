from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)  # this is to avoid any weird edge cases where there are 0's
        for str in strs:
            count = [0] * 26 # for all 26 letters in the alphabet
            for c in str:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(str) #tuples is used since a list cannot be the index of a dict in python
        
        return list(res.values())
    
res = Solution()
print(res.groupAnagrams(strs = ["x"]))