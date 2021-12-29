from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = ([min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])])
                
        result.append(newInterval)
        
        return result
        

run = Solution()
run.insert([[1,3],[6,9]], [2,5])