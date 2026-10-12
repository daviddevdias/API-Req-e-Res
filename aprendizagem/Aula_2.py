import os
import requests

TOKEN = os.environ.get("SMARTTHINGS_TOKEN", "")
if not TOKEN:
    raise SystemExit("Configure SMARTTHINGS_TOKEN antes de executar.")


url = "https://api.smartthings.com/v1"

headers = {
  "Authorization": f"Bearer {TOKEN}"
}


resposta = requests.get(url, headers=headers, timeout=20)


print("STATUS:", resposta.status_code)

