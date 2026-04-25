from typing import Optional, Self

class Node:
    key: int
    val: int
    prev: Optional[Self]
    next: Optional[Self]

    def __init__(self: Self, key: int, val: int, prev: Optional[Self], next: Optional[Self]) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    hashmap: dict[int, Node]
    list_head: Optional[Node]
    list_tail: Optional[Node]
    capacity: int
    n: int

    def __init__(self, capacity: int):
        self.n = 0
        self.capacity = capacity
        self.hashmap = {}
        self.list_head = None
        self.list_tail = None

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.move_node_to_head(node)
        return node.val

    def move_node_to_head(self, node: Node):
        if self.list_head == node:
            return

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
            
        if self.list_tail == node and node.prev is not None:
            self.list_tail = node.prev
        
        node.prev = None
        node.next = self.list_head
        
        if self.list_head:
            self.list_head.prev = node
            
        self.list_head = node

    def insert_start(self, node: Node):
        node.next = None
        node.prev = None

        if self.list_head is None:
            self.list_head = node
            self.list_tail = node
        else: 
            node.next = self.list_head
            self.list_head.prev = node
            self.list_head = node

        self.hashmap[node.key] = node
        self.n += 1

    def evict_end(self):
        if self.list_tail:
            del self.hashmap[self.list_tail.key]

            if self.list_tail.prev:
                self.list_tail.prev.next = None
                self.list_tail = self.list_tail.prev
            else:
                self.list_tail = None
                self.list_head = None 

            self.n -= 1

    def put(self, key: int, val: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = val
            self.move_node_to_head(node)
            return

        if self.n >= self.capacity:
            self.evict_end()

        node = Node(key, val, None, None)
        self.insert_start(node)