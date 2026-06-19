class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        cand1 = None
        cand2 = None
        c1 = 0
        c2 = 0

        result = []
        for num in nums:
            if cand1 == num:
                c1 += 1
            elif cand2 == num:
                c2 += 1
            elif c1 == 0:
                cand1 = num
            elif c2 ==0:
                cand2 = num
            else:
                cand1 -= 1
                cand2 -= 1
        
        ac1=0
        ac2=0

        for num in nums:
            if num == cand1:
                ac1 += 1
            elif num == cand2:
                ac2 += 1
        
        if ac1 > threshold:
            result.append(cand1)
        if ac2 > threshold:
            result.append(cand2)
        
        return result
        

        