from typing import List


def lemonadeChange(bills: List[int]) -> bool:
    fives,tens = 0,0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives < 1:
                return False
            else:
                fives -= 1
                tens += 1
        elif bill == 20:
            if fives >= 1 and tens >= 1:
                fives -= 1
                tens -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True

print(lemonadeChange([5,5,5,10,20]))