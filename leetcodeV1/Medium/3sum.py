from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                
                if threesum > 0:
                    right -= 1
                    
                elif threesum < 0:
                    left += 1
                    
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
            
        return triplets


run = Solution()

run.threeSum([-1,0,1,2,-1,-4])