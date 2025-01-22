def findTheWinner(n: int, k: int) -> int:
  players = [i+1 for i in range(n)]
  idx = 0
  for _ in range(n-1):
    out = ((k-1)+idx) % len(players)
    idx = out
    players.pop(out)

findTheWinner(6, 5)