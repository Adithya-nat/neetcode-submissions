class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0

        for amount in nums:
            current = amount + a
            prev = b

            current = max(current, prev)

            a = prev
            b = current
        
        return current

        