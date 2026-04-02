class Solution:
    def to_alphabet_index(self, word: str) -> int:
        idx = ord(word[0]) - ord('a')
        if idx > 25:
            raise ValueError("char " + word[0] + " is not in alphabet")
        
        return idx
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map: dict[tuple[int, ...], List[str]] = defaultdict(list)

        for word in strs:
            character_arr = [0] * 26
            for c in word:
                character_arr[self.to_alphabet_index(c)] += 1
            anagram_map[tuple(character_arr)].append(word)
        return list(anagram_map.values())
        
                