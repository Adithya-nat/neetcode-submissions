class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        new = sorted(self.nums)
        return new[len(new)-self.k]

        
