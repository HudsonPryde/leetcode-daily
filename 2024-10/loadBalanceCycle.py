from typing import List

def loadBalance(events: List[List[str]], serverPower: List[int]) -> List[str]:
    n = len(serverPower)
    curr = 0
    offline = [False]*n
    curr_power = serverPower[:]
    requests = [0]*n

    def get_next(curr):
        while offline[curr] or curr_power[curr] == 0:
            curr = (curr+1)%n
            if curr == 0:
                for i in range(n):
                    if not offline[i]:
                        curr_power[i] = serverPower[i]
        return curr

    for e in events:
        if e == "REQUEST":
            curr = get_next(curr)
            curr_power[curr] -= 1
            requests[curr] += 1
        else:
            _, i = e.split()
            offline[int(i)] = True
    
    max_req = -1
    max_req_i = -1
    for i in range(n):
        if max_req <= requests[i]:
            max_req = requests[i]
            max_req_i = i
    
    return max_req_i

print(loadBalance(["REQUEST", "REQUEST", "FAIL 2", "REQUEST", "FAIL 3", "REQUEST", "REQUEST"], [1, 2, 1, 2, 1]))