class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [0] * len(height)
        max_r = [len(height) - 1] * len(height)

        for i in range(1, len(height)):
            if height[i] >= height[max_l[i-1]]:
                max_l[i] = i
            else:
                max_l[i] = max_l[i-1]
        
        for i in reversed(range(len(height) - 1)):
            if height[i] >= height[max_r[i+1]]:
                max_r[i] = i
            else:
                max_r[i] = max_r[i+1]

        print(max_l)
        print(max_r)

        area = 0
        for i in range(len(height)):
            min_height = min(height[max_l[i]], height[max_r[i]])
            area += max(min_height - height[i], 0)
        
        return area