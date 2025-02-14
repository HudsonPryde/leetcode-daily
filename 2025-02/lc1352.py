class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        self.zero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.zero = len(self.prefix)
            self.prefix.append(self.prefix[-1])
        else:
            self.prefix.append(num*self.prefix[-1])

    def getProduct(self, k: int) -> int:
        i = len(self.prefix)-k
        if i <= self.zero: return 0
        return self.prefix[-1]//self.prefix[i-1]

obj = ProductOfNumbers()
commands = ["add","getProduct","getProduct","add","add","getProduct","add","getProduct","add","getProduct","add","getProduct","getProduct","add","getProduct"]
values = [[7],[1],[1],[4],[5],[3],[4],[4],[3],[4],[8],[1],[6],[2],[3]]
for c,v in zip(commands,values):
    if c == "add":
        obj.add(v[0])
    else:
        print(obj.getProduct(v[0]))
