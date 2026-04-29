class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars: dict[str, int] = {}

        left = 0

        longest = 0

        for i in range(0, len(s)):
            if s[i] in chars and chars[s[i]] >= left:
                if i - left > longest:
                    longest = i - left
                left = max(left + 1, chars[s[i]] + 1)
            chars[s[i]] = i

        if len(s) - left > longest:
            longest = len(s) - left

        return longest