class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        total = 0
        
        for num in nums:
            total += num
        
        for i, num in enumerate(nums):
            rightSum = total - leftSum - num

            if rightSum == leftSum:
                return i
            
            else:
                leftSum += nums[i]
        
        return -1

        