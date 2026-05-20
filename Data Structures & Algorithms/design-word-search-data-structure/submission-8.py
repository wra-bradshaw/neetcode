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

    def search_subtree(self, key: str, depth: int) -> Self | None:
        if depth == 0:
            if self.val == key:
                return self

            return None

        for child in self.children.values():
            found = child.search_subtree(key, depth - 1)

            if found is not None:
                return found

        return None
    
    def is_at_least_depth(self, depth: int) -> bool:
        print(depth)
        if depth == 0:
            return self.is_word
        for child in self.children.values():
            if child.is_at_least_depth(depth - 1):
                return True
        return False

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
        curr = self.root
        search_depth = 0
        for c in word:
            node: Node | None = None
            if c == ".":
                search_depth += 1
                continue
            if search_depth > 0:
                node = curr.search_subtree(c, search_depth + 1)
                search_depth = 0
            else:
                node = curr.get_child(c)
            if node == None:
                return False
            else:
                curr = node
        if search_depth > 0:
            return curr.is_at_least_depth(search_depth)
        return curr.is_word