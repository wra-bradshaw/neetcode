class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [0]

        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[i-1]:
                stack.append(i)
            else:
                while len(stack) > 0:
                    j = stack[-1]
                    if temperatures[i] > temperatures[j]:
                        stack.pop()
                        res[j] = i-j
                    else:
                        break
                stack.append(i)
        
        return res
