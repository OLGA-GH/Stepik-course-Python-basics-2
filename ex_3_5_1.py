import sys
import requests
import json

params = {"json": "true"}

for line in sys.stdin:
    line = line.rstrip()
    res = requests.get(f"http://numbersapi.com/{line}/math", params=params)
    data = json.loads(res.text)
    if data["found"]:
        print("Interesting")
    else:
        print("Boring")
