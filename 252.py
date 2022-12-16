class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            a, b = intervals[i-1].end, intervals[i].start
            if b < a: 
                return False

        return True