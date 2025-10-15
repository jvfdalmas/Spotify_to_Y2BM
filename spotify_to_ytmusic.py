import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic
import time
import json
import sys

# === CONFIGURAZIONE SPOTIFY ===
# Carica le credenziali da un file esterno per motivi di sicurezza.
# Crea un file 'spotify_credentials.json' usando 'spotify_credentials.json.template' come modello.
try:
    with open('spotify_credentials.json') as f:
        creds = json.load(f)
        SPOTIFY_CLIENT_ID = creds['SPOTIFY_CLIENT_ID']
        SPOTIFY_CLIENT_SECRET = creds['SPOTIFY_CLIENT_SECRET']
except FileNotFoundError:
    print("ERRORE: Il file 'spotify_credentials.json' non è stato trovato.")
    print("Per favore, crea il file usando 'spotify_credentials.json.template' e inserisci le tue credenziali.")
    sys.exit(1)

# L'URI di reindirizzamento che hai impostato nella tua app Spotify.
# Per un'esecuzione locale, di solito è 'http://localhost:8888/callback'
SPOTIFY_REDIRECT_URI = 'http://localhost:8888/callback'

# Lo scope definisce le autorizzazioni che lo script richiede.
# 'user-library-read' per leggere i brani salvati.
# 'playlist-read-private' per leggere le playlist private.
SCOPE = 'user-library-read playlist-read-private'


# === AUTENTICAZIONE SPOTIFY ===
# Assicurati che il file 'spotify_credentials.json' sia stato compilato.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=SCOPE
))

# === AUTENTICAZIONE YOUTUBE MUSIC ===
# Esegui prima lo script 'ytmusic_auth_setup.py' per generare questo file.
ytmusic = YTMusic("headers_auth.json")

# === TRASFERISCI BRANI SALVATI ===
def trasferisci_brani_salvati():
    print("Trasferimento dei brani salvati da Spotify a YouTube Music...")
    results = sp.current_user_saved_tracks(limit=50)
    while results:
        for item in results['items']:
            track = item['track']
            nome = f"{track['name']} {track['artists'][0]['name']}"
            print(f"Cercando: {nome}")
            search_results = ytmusic.search(nome, filter="songs")
            if search_results:
                videoId = search_results[0]['videoId']
                ytmusic.rate_song(videoId, 'LIKE')
                print(f"✓ Aggiunto '{nome}' a Mi Piace su YT Music")
            time.sleep(1)  # Per evitare rate limit
        if results['next']:
            results = sp.next(results)
        else:
            break

# === TRASFERISCI PLAYLIST ===
def trasferisci_playlist():
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        nome_playlist = playlist['name']
        print(f"\nCreazione playlist su YT Music: {nome_playlist}")
        nuova_playlist_id = ytmusic.create_playlist(nome_playlist, "Importata da Spotify")
        tracce = sp.playlist_tracks(playlist['id'])['items']
        for item in tracce:
            track = item['track']
            nome = f"{track['name']} {track['artists'][0]['name']}"
            print(f"  Cercando: {nome}")
            search_results = ytmusic.search(nome, filter="songs")
            if search_results:
                videoId = search_results[0]['videoId']
                ytmusic.add_playlist_items(nuova_playlist_id, [videoId])
                print(f"  ✓ Aggiunto: {nome}")
            time.sleep(1)

# === AVVIO ===
if __name__ == "__main__":
    print("Avvio trasferimento...")
    trasferisci_brani_salvati()
    trasferisci_playlist()
    print("✅ Trasferimento completato!")

