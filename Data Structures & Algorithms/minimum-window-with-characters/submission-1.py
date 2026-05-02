class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq: dict[str, int] = defaultdict(int)

        for c in t:
            t_freq[c] += 1


        s_freq: dict[str, int] = defaultdict(int)

        left = 0
        right = 0
        shortest = ""

        for right in range(len(s)):
            s_freq[s[right]] += 1

            while left < len(s) and (t_freq[s[left]] - s_freq[s[left]]) < 0:
                s_freq[s[left]] -= 1
                left += 1

            if self.compareHashmaps(s_freq, t_freq):
                new_str = s[left:right + 1]

                if len(shortest) == 0 or len(new_str) < len(shortest):
                    shortest = s[left:right + 1]
                s_freq[s[left]] -= 1
                left += 1
        
        return shortest

    def compareHashmaps(self, s_freq: dict[str, int], t_freq: dict[str, int]):
        for k in t_freq:
            if s_freq[k] < t_freq[k]:
                return False
        return True

