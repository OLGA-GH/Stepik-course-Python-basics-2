import json
json_input = json.loads(input())

parents = dict()

for classname in json_input:
    parents[classname['name']] = set() # to avoid duplicates

for each in json_input:
    for classname in parents:
        if classname in each['parents']:
            parents[classname].add(each['name'])

def dfs(graph, start, visited=None): # re-used Depth-first search algorithm
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

for parent in sorted(parents.keys()):
    print(parent, ':', len(dfs(parents, parent)))