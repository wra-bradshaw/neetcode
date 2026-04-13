class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        min_l: list[int] = [-1] * len(heights)
        stack: list[int] = []
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) != 0:
                min_l[i] = stack[-1]
            stack.append(i)

        min_r: list[int] = [len(heights)] * len(heights)
        stack: list[int] = []
        for i in range(len(heights) - 1, -1, -1):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) != 0:
                min_r[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i] * (min_r[i] - min_l[i] - 1))

        return max_area

