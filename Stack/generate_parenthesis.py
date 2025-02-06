from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
        backtrack(0,0)
        return res
    
out = Solution()
res = out.generateParenthesis(n = 3)
print("This is the result: ", res)
print("This is the length of result: ", len(res))

"""The result sequence for different values of n follows the Catalan number sequence."""

