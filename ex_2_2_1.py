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

n = int(input())  # число классов исключений

for _ in range(n):
    inheritance_descr = input().replace(":", " ").split()
    parents.setdefault(inheritance_descr[0], inheritance_descr[1:])

m = int(input())  # количество обрабатываемых исключений

order_list = list()
extra_list = list()

for _ in range(m):
    order_list.append(input())

for curr in range(1, len(order_list)):
    for prev in order_list[:curr]:
        if is_parent(prev, order_list[curr]):
            if order_list[curr] not in extra_list:
                print(order_list[curr])
                extra_list.append(order_list[curr])
