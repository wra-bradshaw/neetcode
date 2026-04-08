class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.minEatingSpeedSearch(piles, h, 1, max(piles))

    def minEatingSpeedSearch(self, piles: List[int], h: int, min_k: int, max_k: int) -> int:
        if min_k == max_k:
            return min_k
        midpoint = min_k + math.floor((max_k - min_k) / 2)
        hrs = self.calculate_num_hours(piles, midpoint)
        if hrs <= h:
            return self.minEatingSpeedSearch(piles, h, min_k, midpoint)
        elif hrs > h:
            return self.minEatingSpeedSearch(piles, h, midpoint + 1, max_k)

    def calculate_num_hours(self, piles: List[int], k: int) -> int:
        hrs = 0
        for pile in piles:
            hrs += math.ceil(pile/k)
        return hrs