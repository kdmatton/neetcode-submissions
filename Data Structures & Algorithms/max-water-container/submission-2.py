class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1 
        maxWater = 0
        while left < right:
            current = min(heights[left], heights[right]) * (right - left)
            maxWater = max(current,maxWater)

            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
            
        return maxWater