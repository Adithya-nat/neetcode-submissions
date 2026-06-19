class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        cuts = []
        for i in range(len(weights)-1):
            cuts.append(weights[i]+weights[i+1])
        
        cuts.sort()

        max = 0
        min = 0

        n = len(cuts)

        max = sum(cuts[-(k-1):])
        min = sum(cuts[:k-1])

        return max - min




        