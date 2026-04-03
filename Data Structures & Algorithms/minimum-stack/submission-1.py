from typing import Self

class Node:
    data: int
    prev_smaller: Self | None
    next_larger: Self | None
    next_node: Self | None

    def __init__(self, data: int) -> None:
        self.data = data
        self.prev_smaller = None
        self.next_larger = None
        self.next_node = None

class MinStack:
    head: Node | None
    head_min: Node | None

    def __init__(self):
        self.head = None
        self.head_min = None

    def push(self, val: int) -> None:
        new_node = Node(val)
        if self.head_min == None:
            self.head_min = new_node
        elif val < self.head_min.data:
            new_node.next_larger = self.head_min
            self.head_min.prev_smaller = new_node
            self.head_min = new_node 
        
        new_node.next_node = self.head
        self.head = new_node

    def pop(self) -> None:
        if self.head == None:
            return
        popping = self.head
        if popping.prev_smaller != None:
            popping.prev_smaller.next_larger = popping.next_larger
        if popping == self.head_min:
            self.head_min = popping.next_larger
        if popping.next_larger != None:
            popping.next_larger.prev_smaller = popping.prev_smaller
        
        self.head = self.head.next_node


    def top(self) -> int | None:
        if self.head != None:
            return self.head.data
        else:
            return -1

    def getMin(self) -> int | None:
        if self.head_min != None:
            return self.head_min.data
        else:
            return -1
        
