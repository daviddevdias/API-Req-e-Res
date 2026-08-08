import requests
import config


def obter_info():

    url = f"{config.API_BASE}/devices"

    headers = {
      "Authorization": f"Bearer {config.TOKEN}"
    }

    resposta = requests.get(url, headers=headers)
    
    dados = resposta.json()
    
    items = dados["items"]
    
    primeiro = items[0]
    
    
    print("Nome:", primeiro["name"])
    print("Label:", primeiro["label"])
    print("ID:", primeiro["deviceId"])
    
    
obter_info()