class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26

        for c in s1:
            s1_freq[self.charToIdx(c)] += 1

        s2_freq = [0] * 26

        window_size = len(s1)

        for right in range(len(s2)):
            s2_freq[self.charToIdx(s2[right])] += 1
            
            if right >= window_size:
                s2_freq[self.charToIdx(s2[right-window_size])] -= 1
            
            if s1_freq == s2_freq:
                return True
        
        return False
        
    
    def charToIdx(self, s: str) -> int:
        return ord(s.lower()) - ord('a')