class Solution:
    def reorganizeString(self, s: str) -> str:

        counts = Counter(s)

        heap = []

        for ch, count in counts.items():
            heapq.heappush(heap, (-count, ch))
        
        previous_count = 0
        previous_char = ""

        result = []

        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)

            count += 1

            if previous_count < 0:
                heapq.heappush(heap, (previous_count, previous_char))

            previous_count = count
            previous_char = char

        return "".join(result) if len("".join(result)) == len(s) else ""

        