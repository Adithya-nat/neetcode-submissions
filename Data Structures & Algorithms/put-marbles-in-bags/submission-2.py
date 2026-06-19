class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        
        cuts = []
        for i in range(len(weights)-1):
            cuts.append(weights[i]+weights[i+1])
        
        cuts.sort()

        if k == 1:
            return 0

        maxVal = 0
        minVal = 0

        n = len(cuts)

        maxVal = sum(cuts[-(k-1):])
        minVal = sum(cuts[:k-1])

        return maxVal - minVal




        