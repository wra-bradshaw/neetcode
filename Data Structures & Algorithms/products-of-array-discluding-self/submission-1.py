class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res: List[int] = [1] * len(nums)
        for i, n_i in enumerate(nums):
            for j, n_j in enumerate(nums):
                if (j == i):
                    print("j == i")
                    continue
                print("multiplying by " + str(n_j))
                res[i] = res[i]*n_j
            print(res)
        return res
