from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        
        if root is None:
            return result
        
        queue = deque()
        queue.append(root)
        
        while queue:
            lenq = len(queue)
            temp_sum = 0
            
            for _ in range(lenq):
                node = queue.popleft()
                temp_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(temp_sum/lenq)
            
        return result
            