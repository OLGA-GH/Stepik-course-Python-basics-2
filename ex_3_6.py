from xml.etree import ElementTree

root = ElementTree.fromstring(input())

colors = {x: 0 for x in ("red", "green", "blue")}

def getChilds(root, level):
    colors[root.attrib["color"]] += level
    level += 1
    for child in root:
        getChilds(child, level)

getChilds(root, 1)

print(colors["red"], colors["green"], colors["blue"])
