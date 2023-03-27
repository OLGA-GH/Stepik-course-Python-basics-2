# Pre-create default namespace
namespaces = {
    "global": {"parent": None, "vars": []},
}


def create(namespace, parent):
    namespaces[namespace] = {"parent": parent, "vars": []}


def add(namespace, var):
    if namespaces.get(namespace):
        namespaces[namespace]["vars"].append(var)


def get(namespace, var):
    while True:
        if var in namespaces[namespace]["vars"]:
            print(namespace)
            break
        elif namespaces[namespace]["parent"]:
            namespace = namespaces[namespace]["parent"]
        else:
            print(None)
            break


n = int(input())

for i in range(n):
    cmd, namespace, arg = input().split()
    if cmd == "create":
        create(namespace, arg)
    if cmd == "add":
        add(namespace, arg)
    if cmd == "get":
        get(namespace, arg)
