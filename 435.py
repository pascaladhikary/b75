class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        notes:  sort, if e[1] < max it overlaps
        crux:   sort by end time
        '''
        intervals.sort(key=lambda x: x[1])
        max_ = float('-inf')
        count = 0
        
        for i, j in intervals:
            if i < max_:
                count += 1
            else:
                max_ = j
        
        return count