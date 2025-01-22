def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal): return False
    goal += goal
    return s in goal

print(rotateString("abcde", "cdeab"))