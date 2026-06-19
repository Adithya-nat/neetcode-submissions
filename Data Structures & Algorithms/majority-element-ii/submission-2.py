class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        freq = {}
        result = set()

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            if(freq[num] > threshold):
                    result.add(num)
        
        return list(result)
        

        