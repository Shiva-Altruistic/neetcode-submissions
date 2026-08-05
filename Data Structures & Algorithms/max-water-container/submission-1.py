class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left , right = 0 , len(heights) - 1
        while left < right:
            area = (right - left) * min(heights[left] , heights[right])
            res = max(res , area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return res




        
        