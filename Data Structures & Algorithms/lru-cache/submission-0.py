class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node 




    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        
        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = selfcache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
        
        else:
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                least_node = self.left.next
                self.remove(least_node)
                del self.cache[least_node.key]
        
