class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0

        for amount in nums:
            current = max(amount + a, b)

            a = b
            b = current
        
        return b

        