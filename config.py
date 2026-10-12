"""Configuração local por variáveis de ambiente."""
import os

TOKEN = os.environ.get("SMARTTHINGS_TOKEN", "")
API_BASE = "https://api.smartthings.com/v1"
SPOTIFY = "https://api.spotify.com/v1/me"
CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", "")

