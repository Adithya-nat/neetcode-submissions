class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open, closed, current):
            if open == n and closed == n:
                result.append("".join(current))
                return

            if open < n:
                current.append("(")
                backtrack(open+1, closed, current)
                current.pop()

            if closed < open:
                current.append(")")
                backtrack(open, closed + 1, current)
                current.pop()

        backtrack(0,0,[])

        return result 
        