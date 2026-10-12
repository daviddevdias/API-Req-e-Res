# Requisições e respostas de APIs com Python

Exercícios de integração com Spotify, Deezer e SmartThings usando `requests`.

## 📁 Arquivos

- `main.py`: busca uma música no Spotify e exibe os resultados.
- `spotify.py`: solicita token com Client Credentials e consulta a busca do Spotify.
- `deezer.py`: busca músicas no Deezer.
- `api.py`: lista informações do primeiro dispositivo retornado pelo SmartThings.
- `config.py`: lê as credenciais de variáveis de ambiente.
- `aprendizagem/`: exemplos introdutórios; alguns ainda precisam de correções.

## 🚀 Preparar e executar

Requisito: Python 3 e credenciais próprias para Spotify e SmartThings.

```bash
git clone https://github.com/daviddevdias/API-Req-e-Res.git
cd API-Req-e-Res
python -m venv .venv
```

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:SPOTIFY_CLIENT_ID = "seu-client-id"
$env:SPOTIFY_CLIENT_SECRET = "seu-client-secret"
python main.py
```

Para o SmartThings:

```powershell
$env:SMARTTHINGS_TOKEN = "seu-token"
python api.py
```

O exemplo Deezer pode ser executado com `python deezer.py`. No Linux ou macOS, ative o ambiente com `source .venv/bin/activate` e configure as variáveis com `export`.

## 🔒 Credenciais e dados

Não grave tokens ou Client Secret no repositório. `.env.example` documenta as variáveis, mas o programa não carrega arquivos .env automaticamente.

O Client ID identifica o aplicativo e não equivale a uma senha; o Client Secret é confidencial. O token SmartThings permite acessar os recursos autorizados pelos seus escopos. Evite publicar nomes e IDs de dispositivos em logs.

Credenciais que já apareceram no GitHub devem ser revogadas e substituídas. Remover valores do código não limpa o histórico nem os arquivos `.pyc` já publicados.

## Limitações

O código depende da disponibilidade das APIs e das permissões da conta. `api.py` assume que há pelo menos um dispositivo. O fluxo Client Credentials do Spotify não autentica um usuário para acessar `/me`.

Os exemplos ainda precisam de tratamento completo de falhas e testes com contas de desenvolvimento.

