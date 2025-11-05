import requests
import json

url = "https://picsum.photos/v2/list?limit=50"
r = requests.get(url)
contenu = r.json()

liste_url = []
for i in contenu:
    if 'r' in i['author'].split()[0]:
        liste_url.append(i['url'])

with open("api.json", "w") as f:
    json.dump(liste_url, f)
