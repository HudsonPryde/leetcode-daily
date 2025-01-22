from typing import List


def survivedRobotsHealths(positions: List[int], healths: List[int], directions: str) -> List[int]:
  positions = list(zip(positions, directions, range(len(positions))))
  positions.sort()
  actions = []

  for robot in positions:
    while actions and actions[-1][1] == "R" and robot[1] == "L":
        if healths[robot[2]] > healths[actions[-1][2]]:
          healths[robot[2]] -= 1
          healths[actions[-1][2]] = 0
          actions.pop()
        elif healths[robot[2]] < healths[actions[-1][2]]:
          healths[robot[2]] = 0
          healths[actions[-1][2]] -= 1
          break
        else:
          healths[robot[2]] = 0
          healths[actions[-1][2]] = 0
          actions.pop()
          break
    if healths[robot[2]] > 0:
      actions.append(robot)

  return [h for h in healths if h > 0]
        
      

# print(survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR"), " expect: [2,17,9,15,10]")
print(survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL"), " expect: [14]")
# print(survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL"), " expect: []")
# print(survivedRobotsHealths([1,3,5,7,9,2,6,10,4,8,11,13,12,14,15,16,17,18,19,20], [100,90,80,70,60,50,40,30,20,10,150,140,130,120,110,100,90,80,70,60], "RLRLRLRLRLRLRLRLRLRL"), " expect: [98,78,59,20,148,109,89,69]")