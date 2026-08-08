import requests

url = "https://api.deezer.com/search"

params = {
  "q": "Linkin Park Numb"
}

resposta = requests.get(url, params=params)

dados = resposta.json()


for music in dados["data"]:
  print(
    music["title"],
    "-",
    music["artist"]["name"]
  )