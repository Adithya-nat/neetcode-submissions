class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        flights = defaultdict(list)

        for s,d in tickets:
            heapq.heappush(flights[s], d)
        
        itenary = []

        def visit(airport):
            while flights[airport]:
                next_airport = heapq.heappop(flights[airport])
                visit(next_airport)
            
            itenary.append(airport)
        
        visit("JFK")

        return itenary[::-1]
                
        