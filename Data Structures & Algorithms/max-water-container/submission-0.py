class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                base = j-i
                height = min(heights[i], heights[j])
                area = base * height
                if area > max_area:
                    max_area = area
        return max_area