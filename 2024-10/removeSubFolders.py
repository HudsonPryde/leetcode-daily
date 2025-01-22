from typing import List


def removeSubfolders(folder: List[str]) -> List[str]:
    folder.sort(key=lambda x: len(x))
    m = set()
    for d in folder:
        dirs = d[1:].split('/')
        acc = ''
        subdir = False
        for k in dirs:
            acc += "/"+k
            if acc in m:
                subdir = True
                break
        if not subdir:
            m.add(d)
    return list(m)

print(removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))