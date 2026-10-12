# Integrações com APIs em Python

Exemplos de requisições HTTP e leitura de respostas de Spotify, Deezer e SmartThings.

## 📌 Funcionalidades

- Busca de músicas no Spotify e Deezer.
- Consulta de dispositivos no SmartThings.
- Autenticação com tokens e credenciais de aplicativo.

## Tecnologias

Python 3 e requests.

## 🚀 Como executar

```bash
git clone https://github.com/daviddevdias/API-Req-e-Res.git
cd API-Req-e-Res
python -m venv .venv
```

No PowerShell, configure o Spotify:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:SPOTIFY_CLIENT_ID = "seu-client-id"
$env:SPOTIFY_CLIENT_SECRET = "seu-client-secret"
python main.py
```

Para consultar dispositivos no SmartThings:

```powershell
$env:SMARTTHINGS_TOKEN = "seu-token"
python api.py
```

O exemplo Deezer é executado com `python deezer.py`. As credenciais são lidas do ambiente; arquivos .env não são carregados automaticamente. O acesso depende das permissões da sua conta.
