from typing import Self
from pprint import pprint

class Node:
    value: str
    children: dict[str, Self]
    is_word: bool

    def __init__(self, value: str, is_word: bool):
        self.value = value
        self.is_word = is_word
        self.children = {}

    def add_child(self, node: Self):
        self.children[node.value] = node

    def get_child(self, value: str) -> Self | None:
        return self.children[value] if value in self.children else None


class PrefixTree:
    root: Node

    def __init__(self):
        self.root = Node("", False)

    def insert(self, word: str) -> None:
        curr = self.root

        for i in range(0, len(word)):
            res = curr.get_child(word[i])
            
            node: Node | None = None
            if res == None:
                node = Node(word[i], False)
                curr.add_child(node)
            else:
                node = res

            if i == len(word) - 1 and node != None:
                node.is_word = True

            curr = node
        
    def search(self, word: str) -> bool:
        res = self.__search(word)
        return res != None and res.is_word
        
    def startsWith(self, prefix: str) -> bool:
        return self.__search(prefix) != None

    def __search(self, word: str) -> Node | None:
        curr = self.root
        for c in word:
            new = curr.get_child(c)
            if new == None:
                return None
            curr = new
        return curr
        

    