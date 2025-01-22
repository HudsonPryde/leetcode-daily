class AllOne:
    class Node:
        def __init__(self, key, prev, next):
            self.value = 1
            self.key = key
            self.prev = prev
            self.next = next
        def swap(self, target):
            a,b,c,d = self.prev, self, target, target.next
            if a:
                a.next = c
            if d:
                d.prev = b
            b.prev = c
            b.next = d
            c.prev = a
            c.next = b
        def inc(self):
            self.value += 1
            while self.next and self.value > self.next.value:
                self.swap(self.next)
        def dec(self):
            self.value -= 1
            while self.prev and self.value < self.prev.value:
                self.prev.swap(self.prev.next)
            if self.value == 0:
                if self.next:
                    self.next.prev = self.prev

                if self.prev:
                    self.prev.next = self.next

    def __init__(self):
        self.cache = {}
        self.head = None
        self.tail = None

    def inc(self, key: str) -> None:
        if key not in self.cache:
            self.cache[key] = self.Node(key, None, self.tail)
            if not self.head:
                self.head = self.cache[key]
            if self.tail:
                self.tail.prev = self.cache[key]
            self.tail = self.cache[key]
        else:
            if self.cache[key].next and self.cache[key].value+1 > self.cache[key].next.value:
                if self.tail.key == key:
                    self.tail = self.cache[key].next
            self.cache[key].inc()
            if self.head:
                if self.cache[key].value > self.head.value:
                    self.head = self.cache[key]
            else:
                self.head = self.cache[key]

    def dec(self, key: str) -> None:
        if self.head.key == key:
            if self.cache[key].prev and self.cache[key].value-1 < self.cache[key].prev.value:
                self.head = self.cache[key].prev
        self.cache[key].dec()
        if self.cache[key].value == 0:
            if key == self.tail.key:
                self.tail = self.cache[key].next
            del self.cache[key]

    def getMaxKey(self) -> str:
        if self.head:
            return self.head.key
        else:
            return ""

    def getMinKey(self) -> str:
        if self.tail:
            return self.tail.key
        else:
            return ""

obj = AllOne()
obj.inc("a")
obj.inc("b")
obj.inc("c")
obj.inc("d")
obj.inc("a")
obj.inc("d")
obj.getMaxKey()
obj.getMinKey()
obj.inc("c")
obj.getMaxKey()
obj.getMinKey()
obj.inc("b")
obj.dec("d")
obj.dec("d")
obj.getMaxKey()
obj.getMinKey()