class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map: dict[int, int] = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        freq: List[List[int]] = [[] for _ in range(len(nums))]

        for key, val in freq_map.items():
            freq[val-1].append(key)

        res = []
        for nums in reversed(freq):
            if len(res) >= k:
                return res
            res.extend(nums)

        return res


        