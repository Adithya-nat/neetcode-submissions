class Solution:
    def distanceScore(self, point):
        x=point[0]
        y=point[1]
        return x*x + y*y
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        points.sort(key=self.distanceScore)
        return points[:k]