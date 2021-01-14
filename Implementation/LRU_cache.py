class DoubleLL:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = dict()
        self.head = DoubleLL()
        self.tail = DoubleLL()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
        
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        n = self.cache.get(key, None)
        if not n:
            return -1
        self._move_to_head(n)
        return n.value
    
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
    
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = DoubleLL()
            new_node.key = key
            new_node.value = value
            
            self.cache[key] = new_node
            self._add_node(new_node)
            
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)
