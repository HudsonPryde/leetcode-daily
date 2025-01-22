import collections

def solution(hand, groupSize):
  # group size must divide hand size evenly
  if len(hand)%groupSize != 0:
    return False
  hand.sort()
  dq = collections.deque([])

  #print(card_ct)
  for card in hand:
      #print(card)
      if len(dq) >0:
          if dq[-1][1] == card -1:
              item = dq.pop()
              item[0] += 1
              item[1] = card
          elif dq[-1][1] == card:
              item = [1,card]
          else:
              return False # in this case there will not be anything to fill the open straight
      else:
          item = [1,card]
  
      if item[0] < groupSize:
          dq.appendleft(item) # move it to left so we can deal with new new ones 
  return len(dq) == 0

print(solution([9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11], 10))