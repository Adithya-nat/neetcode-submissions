class Solution:
    def distanceScore(self, point):
        x=point[0]
        y=point[1]
        return x*x + y*y
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        output =[]

        for point in points:
            dist = self.distanceScore(point)
            heapq.heappush(heap, (-dist, point))

            if len(heap) > k:
                heapq.heappop(heap)
        
        # for item in heap:
        #     dist = item[0]
        #     point = item[1]
        #     output.append(point)
        # return output 

        for dist, point in heap:
            output.append(point)

        return output
        

            
