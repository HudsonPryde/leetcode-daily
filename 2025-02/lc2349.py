from heapq import heappush, heappop
from collections import defaultdict
class NumberContainers:

    def __init__(self):
        self.nums = {}
        self.mins = defaultdict(list)
        

    def change(self, index: int, number: int) -> None:
        self.nums[index] = number
        heappush(self.mins[number], index)


    def find(self, number: int) -> int:
        if not self.mins[number]: return -1
        index = self.mins[number][0]
        while (self.nums[index] != number) and self.mins[number]:
            heappop(self.mins[number])
            if self.mins[number]:
                index = self.mins[number][0]
            else:
                break
        return -1 if self.nums[index] != number else index

obj = NumberContainers()
commands = ["change","change","find","find","find","change","find","find","change","find","change","change","change","find","find","change","find","change","change","change"]
data = [[25,50],[56,31],[50],[50],[43],[30,50],[31],[43],[25,20],[50],[56,43],[68,31],[56,31],[20],[43],[25,43],[43],[56,31],[54,43],[63,43]]
for c,v in zip(commands,data):
    if c == "change":
        a,b = v
        obj.change(a,b)
    else:
        a = v[0]
        print(obj.find(a))

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)