import requests

TOKEN = "SEUTOKEN"


url = "https://api.smartthings.com/v1"

headers = {
  "Authorization": f"Bearer {TOKEN}"
}


resposta = requests.get(url, headers=headers)


print(headers)
