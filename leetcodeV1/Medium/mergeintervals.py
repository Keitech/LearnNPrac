from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        
        if not intervals:
            return result
        
        intervals.sort(key=lambda x:x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                result.append([start,end])
                start = interval[0]
                end = interval[1]
        
        result.append([start,end])
        
        return result

run = Solution()

run.merge([[1,3],[2,6],[8,10],[15,18]])