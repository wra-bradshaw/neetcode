from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeBottomUp(coins, amount)
    
    def coinChangeBottomUp(self, coins: list[int], amount: int) -> int:
        table = [0] * (amount + 1)

        for curr in range(1, amount + 1):
            table[curr] = -1
            min_coins = sys.maxsize

            for coin in coins:
                if coin > curr:
                    continue
            
                remainder = curr-coin
                n_coins = 1 + table[remainder]
                if table[remainder] != -1 and n_coins < min_coins:
                    min_coins = n_coins
            
            table[curr] = min_coins if min_coins != sys.maxsize else -1

        return table[amount]

    @lru_cache(maxsize=None)
    def coinChangeTopDown(self, coins: list[int], amount: int) -> int:
        pass
        
        