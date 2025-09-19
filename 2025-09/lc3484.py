from collections import defaultdict
class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        terms = formula[1:].split("+")
        res = 0
        for x in terms:
            if x[0].isalpha():
                res += self.cells[x]
            else:
                res += int(x)
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)