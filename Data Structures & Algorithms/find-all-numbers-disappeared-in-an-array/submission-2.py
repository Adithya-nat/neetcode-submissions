class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            nums[i] = - abs(nums[i])
        
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i+1)
        
        return result
                
        