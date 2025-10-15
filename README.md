# Trasferimento da Spotify a YouTube Music

Questo progetto contiene una serie di script Python per trasferire le tue playlist e i tuoi brani salvati da Spotify a YouTube Music.

## Prerequisiti

Prima di iniziare, assicurati di avere Python installato sul tuo sistema. Avrai anche bisogno delle seguenti librerie Python:

- `spotipy`
- `ytmusicapi`

Puoi installarle usando pip:

```bash
pip install spotipy ytmusicapi
```

## Come si usa

Segui questi passaggi per trasferire la tua musica.

### Passaggio 1: Configurare l'Autenticazione di YouTube Music

Per prima cosa, devi fornire il tuo cookie di autenticazione di YouTube Music. Questo processo ora è manuale e não richiede di incollare nulla nel terminale.

1.  Crea una copia del file `headers_auth.json.template` e rinominala in `headers_auth.json`.
2.  Apri YouTube Music nel tuo browser e apri gli **Strumenti per sviluppatori** (F12).
3.  Vai alla scheda **Network** (Rete), ricarica la pagina e trova una richiesta `browse`.
4.  Nei **Request Headers** di quella richiesta, trova la riga `cookie`.
5.  Copia l'intero valore del cookie (è una stringa molto lunga).
6.  Apri il tuo file `headers_auth.json` e incolla la stringa del cookie al posto di `"INCOLLA_QUI_L_INTERO_COOKIE_DI_YOUTUBE_MUSIC"`. Assicurati di mantenere le virgolette.

Il risultato dovrebbe essere simile a questo:
```json
{
  "Cookie": "HSID=...; SSID=...; ...",
  "x-goog-authuser": "0",
  ...
}
```

### Passaggio 2: Configurare le Credenziali dell'API di Spotify

Successivamente, devi configurare le tue credenziali per l'API di Spotify usando un file di testo separato per motivi di sicurezza.

1.  Crea una copia del file `spotify_credentials.txt.template` e rinominala in `spotify_credentials.txt`.
2.  Vai alla tua [Dashboard per sviluppatori di Spotify](https://developer.spotify.com/dashboard) e accedi.
3.  Crea una nuova app (o usane una esistente).
4.  Dopo aver creato l'app, vai su "Settings" e copia il tuo **Client ID** e **Client Secret**.
5.  Apri il file `spotify_credentials.txt` e incolla il tuo Client ID e Client Secret dopo i segni di uguale:
    ```
    SPOTIFY_CLIENT_ID=IL_TUO_CLIENT_ID_QUI
    SPOTIFY_CLIENT_SECRET=IL_TUO_CLIENT_SECRET_QUI
    ```
6.  Nelle impostazioni della tua app Spotify, aggiungi un "Redirect URI". Per un'esecuzione locale, `http://localhost:8888/callback` è una scelta comune. Assicurati che questo URI corrisponda a quello nello script `spotify_to_ytmusic.py`.

**Importante:** Il file `spotify_credentials.txt` è già nel `.gitignore`, quindi le tue credenziali non verranno caricate su Git.

### Passaggio 3: Eseguire il Trasferimento

Ora che tutto è configurato, puoi avviare il trasferimento.

1.  Esegui lo script principale:
    ```bash
    python spotify_to_ytmusic.py
    ```
2.  La prima volta che lo esegui, si aprirà una pagina del browser per autorizzare l'accesso al tuo account Spotify. Accedi e autorizza l'app.
3.  Lo script inizierà a trasferire i tuoi brani salvati e le tue playlist. Potrebbe volerci del tempo a seconda delle dimensioni della tua libreria.

## File del Progetto

-   `spotify_to_ytmusic.py`: Lo script principale che esegue il trasferimento.
-   `test_cookie.py`: Uno script di utilità per verificare se l'autenticazione di YouTube Music (`headers_auth.json`) funziona correttamente.
-   `.gitignore`: Assicura che i file sensibili (`headers_auth.json`, `spotify_credentials.txt`) non vengano caricati su Git.
-   `headers_auth.json.template`: Modello per il file di autenticazione di YouTube Music.
-   `spotify_credentials.txt.template`: Modello per il file di credenziali di Spotify.