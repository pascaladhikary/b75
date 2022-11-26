from heapq import *
class MedianFinder:
    '''
    notes:  case: num > min(right), add to right else left
            balance when necessary
    crux:   heaps
    '''
    def __init__(self):
        self.l = []
        self.r = []
        
    def addNum(self, num: int) -> None:
        if self.r and num > self.r[0]:
            heappush(self.r, num)
        else:
            heappush(self.l, -num)
        
        l1, l2 = len(self.l), len(self.r)
        if l1 > l2 + 1:
            heappush(self.r, -heappop(self.l))
        elif l2 > l1 + 1:
            heappush(self.l, -heappop(self.r))

    def findMedian(self) -> float:
        l1, l2 = len(self.l), len(self.r)
        
        if l1 < l2:
            return self.r[0]
        elif l1 > l2:
            return -self.l[0]
        else:
            return (-self.l[0] + self.r[0])/2