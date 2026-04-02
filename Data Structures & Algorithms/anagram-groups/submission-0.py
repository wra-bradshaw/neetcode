class Solution:
    def is_anagram(self, str_a: str, str_b: str) -> bool:
        if len(str_a) != len(str_b):
            return False
        if str_a == str_b:
            return True
        
        distrib: dict[str, int] = {}

        for c in str_a:
            distrib[c] = distrib.get(c, 0) + 1
        
        for c in str_b:
            if c not in distrib:
                return False
            distrib[c] -= 1
            if distrib[c] < 0:
                return False
        
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        used: List[bool] = [False] * len(strs)

        out: List[List[str]] = []
        for i, word_a in enumerate(strs):
            if used[i]:
                continue
            
            used[i] = True
            anagrams = [word_a]
            for j in range(i+1, len(strs)):
                word_b = strs[j]
                if used[j]:
                    continue
                if self.is_anagram(word_a, word_b):
                    used[j] = True
                    anagrams.append(word_b)
            out.append(anagrams)

        return out        