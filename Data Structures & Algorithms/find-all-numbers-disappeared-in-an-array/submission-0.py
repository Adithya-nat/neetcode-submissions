class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numKey = {}

        for i, num in enumerate(nums):
            if num not in numKey:
                numKey[num] = i

        result = []
        
        for i, num in enumerate(nums, 1):
            if i not in numKey:
                result.append(i)
        
        return result
                
        