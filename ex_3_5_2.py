import requests
import json
import sys

client_id = '0955531481ed027de82f'
client_secret = 'c68dc852aadbd6ad213996842b171b33'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

painters = []

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    line = line.rstrip()
    # инициируем запрос с заголовком
    res = requests.get(f"https://api.artsy.net/api/artists/{line}", headers=headers)
    data = json.loads(res.text)
    painters.append({'name': data['sortable_name'], 'birthday': data['birthday']})

for painter in sorted(painters, key=lambda x: (x['birthday'], x['name'])):
    print(painter['name'])