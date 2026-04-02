class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            i_c = s[i].lower()
            j_c = s[j].lower()

            if not i_c.isalnum():
                i += 1
                continue
            
            if not j_c.isalnum():
                j -= 1
                continue

            if i_c != j_c:
                return False
            
            i += 1
            j -= 1
        
        return True

        