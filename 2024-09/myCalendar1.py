class MyCalendar:

    def __init__(self):
        self.calendar = {}

    def book(self, start: int, end: int) -> bool:
        self.calendar[start] = 1
        self.calendar[end] = -1
        b = 0
        for i in range(start, end):
            if i in self.calendar:
                b += self.calendar[i]
                if b == 3:
                    self.calendar[start] = 0
                    self.calendar[end] = 0
                    return False
        return True
        
c = MyCalendar()
times = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
for b in times:
    c.book(b[0],b[1])
print(c.booked_times)