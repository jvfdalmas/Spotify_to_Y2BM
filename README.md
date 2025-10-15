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

Per prima cosa, devi autenticarti con YouTube Music.

1.  Esegui lo script `ytmusic_auth_setup.py`:
    ```bash
    python ytmusic_auth_setup.py
    ```
2.  Lo script ti fornirà istruzioni dettagliate su come ottenere il tuo "cookie" dal browser. Segui attentamente le istruzioni.
3.  Dopo aver incollato il cookie, verrà creato un file `headers_auth.json`. Questo file contiene le tue credenziali di autenticazione e non deve essere condiviso.

**Nota:** Devi eseguire questo passaggio solo una volta.

### Passaggio 2: Configurare le Credenziali dell'API di Spotify

Successivamente, devi configurare le tue credenziali per l'API di Spotify usando un file separato per motivi di sicurezza.

1.  Crea una copia del file `spotify_credentials.json.template` e rinominala in `spotify_credentials.json`.
2.  Vai alla tua [Dashboard per sviluppatori di Spotify](https://developer.spotify.com/dashboard) e accedi.
3.  Crea una nuova app (o usane una esistente).
4.  Dopo aver creato l'app, vai su "Settings" e copia il tuo **Client ID** e **Client Secret**.
5.  Apri il file `spotify_credentials.json` e incolla il tuo Client ID e Client Secret nei campi corrispondenti:
    ```json
    {
      "SPOTIFY_CLIENT_ID": "IL_TUO_CLIENT_ID_QUI",
      "SPOTIFY_CLIENT_SECRET": "IL_TUO_CLIENT_SECRET_QUI"
    }
    ```
6.  Nelle impostazioni della tua app Spotify, aggiungi un "Redirect URI". Per un'esecuzione locale, `http://localhost:8888/callback` è una scelta comune. Assicurati che questo URI corrisponda a quello nello script `spotify_to_ytmusic.py`.

**Importante:** Il file `spotify_credentials.json` è già nel `.gitignore`, quindi le tue credenziali non verranno caricate su Git.

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
-   `ytmusic_auth_setup.py`: Script per configurare l'autenticazione di YouTube Music.
-   `test_cookie.py`: Uno script di utilità per verificare se l'autenticazione di YouTube Music (`headers_auth.json`) funziona correttamente.
-   `.gitignore`: Assicura che il file sensibile `headers_auth.json` non venga caricato su Git.