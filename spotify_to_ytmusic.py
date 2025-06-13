import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic
import time

# === CONFIGURAZIONE ===
SPOTIFY_CLIENT_ID = ''
SPOTIFY_CLIENT_SECRET = ''
SPOTIFY_REDIRECT_URI = ''
SCOPE = ''

# === AUTENTICAZIONE SPOTIFY ===
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=SCOPE
))

# === AUTENTICAZIONE YOUTUBE MUSIC ===
ytmusic = YTMusic("headers_auth.json")  # Vedi guida sotto

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

