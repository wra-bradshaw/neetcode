class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_s: dict[str, int] = {}

        seen_t: dict[str, int] = {}

        for char in s:
            if char in seen_s:
                seen_s[char] = seen_s[char] + 1
            else:
                seen_s[char] = 1
        
        for char in t:
            if char in seen_s:
                if char in seen_t:
                    if seen_t[char] >= seen_s[char]:
                        return False
                    else:
                        seen_t[char] = seen_t[char] + 1
                else:
                    seen_t[char] = 1
            else:
                return False 
        
        return True


        
        