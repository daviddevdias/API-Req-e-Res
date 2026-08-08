import requests
import base64
import config


def pegar_token():

    auth = f"{config.CLIENT_ID}:{config.CLIENT_SECRET}"

    encoded = base64.b64encode(
        auth.encode()
    ).decode()

    resposta = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {encoded}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "grant_type": "client_credentials"
        }
    )

    return resposta.json()["access_token"]



def buscar_musica(nome):

    token = pegar_token()

    resposta = requests.get(
        "https://api.spotify.com/v1/search",
        headers={
            "Authorization": f"Bearer {token}"
        },
        params={
            "q": nome,
            "type": "track",
            "limit": 5
        }
    )

    print("STATUS:", resposta.status_code)
    print("RESPOSTA:", resposta.text)

    return resposta.json()