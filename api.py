import requests
import config


def obter_info():

    if not config.TOKEN:
        raise SystemExit("Configure SMARTTHINGS_TOKEN antes de executar.")

    url = f"{config.API_BASE}/devices"

    headers = {
      "Authorization": f"Bearer {config.TOKEN}"
    }

    resposta = requests.get(url, headers=headers, timeout=20)
    resposta.raise_for_status()
    
    dados = resposta.json()
    
    items = dados["items"]
    
    primeiro = items[0]
    
    
    print("Nome:", primeiro["name"])
    print("Label:", primeiro["label"])
    print("ID:", primeiro["deviceId"])
    
    
obter_info()
