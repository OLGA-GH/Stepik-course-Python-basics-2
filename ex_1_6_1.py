parents = {}

def is_parent(parent, child):
    if child in parents.keys():
        if child == parent or parent in parents[child]:
            return True
        elif not parents[child]:
            return False
        else:
            for each in parents[child]:
                if each in parents.keys() and is_parent(parent, each):
                    return True
    return False

n = int(input())

for _ in range(n):
    inheritance_descr = input().replace(":", " ").split()
    parents.setdefault(inheritance_descr[0], inheritance_descr[1:])

q = int(input())

for _ in range(q):
    parent, child = input().split()
    print("Yes" if is_parent(parent, child) else "No")
