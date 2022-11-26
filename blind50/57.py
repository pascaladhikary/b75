class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        notes:  insert, then merge... could be faster
        '''
        def mergeIntervals(intervals):
            l, r = intervals[0]
            res = []
            
            for i in range(1, len(intervals)):
                x0, x1 = intervals[i]
                if x0 <= r:
                    r = max(r, x1)
                else:
                    res.append([l, r])
                    l, r = x0, x1
                if i == len(intervals) - 1: res.append([l, r])
            return res
        
        if not intervals:
            return [newInterval]
        
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]: intervals.insert(i, newInterval); break
            elif i == len(intervals) - 1: intervals.append(newInterval); break
                
        return mergeIntervals(intervals)