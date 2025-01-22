def numWaterBottles(numBottles: int, numExchange: int) -> int:
  total = numBottles
  empty = numBottles
  while empty >= numExchange:
    full = empty // numExchange
    total += full
    empty = (empty % numExchange) + full
  return total

def numWaterBottlesO1(numBottles: int, numExchange: int) -> int:
  return numBottles + ((numBottles - 1)//(numExchange - 1))

print(numWaterBottlesO1(9, 3))