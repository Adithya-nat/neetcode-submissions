class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        nums.sort()
        temp = []

        for i in range(n-1):
            temp.append(nums[i+1] - nums[i])
        
        prev_one = False
        res = 0
        count = 0

        for i, val in enumerate(temp):
            if val == 1 or val == 0 or val == -1:
                if not prev_one:
                    prev_one = True
                count += 1
                res = max(count, res)
            else:
                prev_one = False
                count = 0
        
        return res
                    



        