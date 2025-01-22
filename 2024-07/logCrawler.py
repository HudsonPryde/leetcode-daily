from typing import List


def minOperations(logs: List[str]) -> int:
  depth = 0
  for op in logs:
      if op == "./":
          continue
      elif op == "../":
          depth = max(depth-1, 0)
      else:
          depth += 1
  return max(depth, 0)