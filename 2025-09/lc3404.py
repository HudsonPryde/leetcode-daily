from typing import List
from heapq import heappop, heappush

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {tasks[i][1]: [tasks[i][0], tasks[i][2]] for i in range(len(tasks))}
        self.exec = []
        for u,t,p in tasks:
            heappush(self.exec, (-p,-t,u))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = [userId, priority]
        heappush(self.exec, (-priority,-taskId,userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasks[taskId][1] = newPriority
        heappush(self.exec, (-newPriority,-taskId,self.tasks[taskId][0]))

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]

    def execTop(self) -> int:
        if not self.exec: return -1
        while -self.exec[0][1] not in self.tasks or -self.exec[0][0] != self.tasks[-self.exec[0][1]][1] or self.exec[0][2] != self.tasks[-self.exec[0][1]][0]:
            heappop(self.exec)
            if not self.exec: return -1
        del self.tasks[-self.exec[0][1]]
        return heappop(self.exec)[2]


# Your TaskManager object will be instantiated and called as such:
tasks = [[1,104,8]]
obj = TaskManager(tasks)
# obj.add(4,104,5)
# obj.edit(102,9)
# print(obj.execTop())
obj.rmv(104)
# obj.add(50,101,8)
print(obj.execTop())