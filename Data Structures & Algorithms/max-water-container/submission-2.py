class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        lower = 0
        upper = len(heights) - 1

        while lower < upper:
            base = upper - lower
            height = min(heights[upper], heights[lower])
            area = base*height
            if area > max_area:
                max_area = area

            if heights[lower] < heights[upper]:
                lower += 1
            elif heights[upper] < heights[lower]:
                upper -= 1
            else:
                lower += 1
                upper -= 1
        
        return max_area


