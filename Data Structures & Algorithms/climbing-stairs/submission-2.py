class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        oneStep = 2
        twoStep = 1

        for i in range(3,n+1):
            current = oneStep + twoStep
            twostep = oneStep
            oneStep = current
        
        return oneStep
        