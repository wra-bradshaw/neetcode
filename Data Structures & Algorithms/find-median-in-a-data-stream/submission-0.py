class MedianFinder:
    lower: list[int] # max heap
    upper: list[int] # min heap

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if len(self.upper) == 0:
            heapq.heappush(self.upper, num)
            return

        upper = self.upper[0]

        if num >= upper:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush_max(self.lower, num)
        
        self._rebalance()

        print(self.lower, self.upper)

    def _rebalance(self) -> None:
        while len(self.lower) - len(self.upper) > 1:
            # remove items from lower add to upper
            heapq.heappush(self.upper, heapq.heappop_max(self.lower))
        while len(self.upper) - len(self.lower) > 1:
            # remove items from upper add to lower
            heapq.heappush_max(self.lower, heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return self.lower[0]
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
        else:
            return (self.lower[0] + self.upper[0])/2

            
        
        