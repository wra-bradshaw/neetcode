class Solution:
    # [0, 0], (1, 2), 3, (4, 5)
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict: dict[int, int] = {}

        for num in nums:
            num_dict[num] = -1
        
        for k in num_dict:
            num_dict[k] = 1
            j = k
            while True:
                if j+1 in num_dict:
                    if num_dict[j+1] != -1:
                        num_dict[k] += num_dict[j+1]
                        break

                    num_dict[k] += 1
                    j += 1
                else:
                    break
        
        max_val = 0
        for k in num_dict:
            if num_dict[k] > max_val:
                max_val = num_dict[k]

        return max_val


        