class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)

        leftSize = ( m + n + 1) // 2

        low = 0
        high = m

        while low <= high:
            i = (low + high) // 2
            j = leftSize - i

            aleft = nums1[i-1] if i > 0 else float("-inf")
            aright = nums1[i] if i < m else float("inf")

            bleft = nums2[j-1] if j > 0 else float("-inf")
            bright = nums2[j] if j < n else float("inf")

            if aleft <= bright and bleft <= aright:
                if (m + n) % 2 == 1:
                    return max(aleft, bleft)
                
                lleft = max(aleft, bleft)
                lright = min(aright, bright)

                return (lleft + lright) / 2

            if aleft > bright:
                high = i - 1
            
            else:
                low = i + 1
        