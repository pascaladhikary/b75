class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        notes:  sort, then lptr, rptr
                two odd cases: last element, and [1,4], [2,3]
        '''
        intervals.sort()
        res = []
        l, r = intervals[0][0], intervals[0][1]
        
        for i, p in enumerate(intervals):
            if p[0] > r:
                res.append((l, r))
                l, r = p[0], p[1]
            else:
                if p[1] > r: r = p[1]
                
            if i == len(intervals)-1:
                res.append((l, r))
            
        return res