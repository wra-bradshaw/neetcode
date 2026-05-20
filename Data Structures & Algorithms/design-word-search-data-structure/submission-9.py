from typing import Self

class Node:
    val: str
    children: dict[str, Self]
    is_word: bool

    def __init__(self, val: str):
        self.val = val
        self.children = {}
        self.is_word = False

    def add_child(self, node: Self):
        self.children[node.val] = node
    
    def get_child(self, key: str) -> Self | None:
        return self.children[key] if key in self.children else None


class WordDictionary:
    root: Node

    def __init__(self):
        self.root = Node("")
        
    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            node = curr.get_child(c)
            if node == None:
                node = Node(c)
                curr.add_child(node)
            curr = node

        curr.is_word = True
        
    def search(self, word: str) -> bool:
        def dfs(node: Node, i: int) -> bool:
            if i == len(word):
                return node.is_word

            c = word[i]

            if c == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            child = node.get_child(c)
            if child is None:
                return False

            return dfs(child, i + 1)

        return dfs(self.root, 0)