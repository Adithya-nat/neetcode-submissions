class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0

        curMax = 0
        maxSum = nums[0]

        curMin = 0
        minSum = nums[0]

        for num in nums:
            curMax = max(num, num + curMax)
            maxSum = max(curMax, maxSum)

            curMin = min(num, num + curMin)
            minSum = min(curMin, minSum)

            total += num

        if maxSum < 0:
            return maxSum
        
        return max(maxSum, total - minSum)

        