class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        current_sum = 0
        count = 0

        pref_freq = {0: 1}

        for num in nums:
            current_sum += num
            
            prev_sum = current_sum - k
            
            count += pref_freq.get(prev_sum, 0)

            pref_freq[current_sum] = pref_freq.get(current_sum, 0) + 1

            
        return count


        