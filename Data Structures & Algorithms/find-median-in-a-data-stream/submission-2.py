class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        val=-heapq.heappop(self.small)
        heapq.heappush(self.large,val)

        if len(self.large)>len(self.small):
            val2=heapq.heappop(self.large)
            heapq.heappush(self.small,-val2)
        

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        else:
            return (-1*self.small[0]+self.large[0])/2

        
        