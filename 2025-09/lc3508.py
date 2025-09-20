from collections import deque,defaultdict
from typing import List
from bisect import bisect_left, bisect_right
# on memeory limit oldest packet is removed
# do not add duplicates, if dup return false
# forward packet is FIFO
# getCount range is incluvise
class Router:

    def __init__(self, memoryLimit: int):
        self.content = set()
        self.packets = deque()
        self.dest = defaultdict(deque)
        self.limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source,destination,timestamp)
        if packet in self.content:
            return False
        elif len(self.packets) == self.limit:
            rm = self.packets.popleft()
            self.dest[rm[1]].popleft()
            self.content.remove(rm)
        self.content.add(packet)
        self.packets.append(packet)
        self.dest[destination].append(packet)
        return True

    def forwardPacket(self) -> List[int]:
        if self.packets:
            packet = self.packets.popleft()
            self.content.remove(packet)
            self.dest[packet[1]].popleft()
            return list(packet)
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if len(self.dest[destination]) == 0:
            return 0
        start = bisect_left(self.dest[destination],startTime,key=lambda x: x[2])
        end = bisect_right(self.dest[destination],endTime,key=lambda x: x[2])
        return end-start


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)