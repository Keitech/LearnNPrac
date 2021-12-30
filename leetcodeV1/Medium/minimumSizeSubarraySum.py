import math
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = math.inf
        total = 0
        win_start = 0
        
        for win_end in range(len(nums)):
            total += nums[win_end]
            
            while total >= target:
                min_len = min(win_end - win_start + 1, min_len)
                total -= nums[win_start]
                win_start += 1
        
        if min_len == math.inf:
            return 0
                
        return min_len
        

run = Solution()

run.minSubArrayLen(7, [2,3,1,2,4,3])