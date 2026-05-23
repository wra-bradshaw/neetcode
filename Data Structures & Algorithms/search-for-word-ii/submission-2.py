from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.buildTrie(words)

        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(i: int, j: int, node: TrieNode):
            char = board[i][j]

            if char not in node.children:
                return

            next_node = node.children[char]

            if next_node.word is not None:
                res.append(next_node.word)
                next_node.word = None  # prevents duplicate results

            board[i][j] = "#"  # mark visited

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
            ]

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (
                    0 <= ni < rows
                    and 0 <= nj < cols
                    and board[ni][nj] != "#"
                ):
                    dfs(ni, nj, next_node)

            board[i][j] = char  # unmark visited

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return res

    def buildTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode()

        for word in words:
            curr = root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]

            curr.word = word

        return root