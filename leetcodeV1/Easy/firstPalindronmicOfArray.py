from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

run = Solution()

run.firstPalindrome(["abc","car","ada","racecar","cool"])