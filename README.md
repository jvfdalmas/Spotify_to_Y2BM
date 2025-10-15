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

### Passaggio 1: Configurare l'Autenticazione di YouTube Music (macOS)

Questo progetto include uno script per automatizzare la configurazione usando la clipboard del macOS.

1.  **Apri il browser Brave** (o qualsiasi browser baseado in Chromium) e vai su `music.youtube.com`.
2.  **Apri gli Strumenti per Sviluppatori** (Cmd+Option+I) e vai alla scheda **Network** (Rete).
3.  **Trova una richiesta `browse`:** Ricarica la pagina o naviga nella tua libreria. Filtra per `browse` nella barra di ricerca della scheda Network per trovarla facilmente.
4.  **Copia i cabeçalhos de requisição:**
    *   Clicca sulla richiesta `browse`.
    *   Nella scheda **Headers**, scorri verso il basso fino alla sezione **Request Headers**.
    *   **Copia l'intero blocco di testo** dei cabeçalhos de requisição.
5.  **Esegui lo script di configurazione:** Apri il terminale e esegui il seguente comando. Questo invierà il contenuto della tua clipboard direttamente allo script:
    ```bash
    pbpaste | python setup_ytmusic.py
    ```
6.  Se tutto va a buon fine, verrà creato un file `headers_auth.json` e você estará pronto para o próximo passo.

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
-   `setup_ytmusic.py`: Script per automatizzare la configurazione dell'autenticazione di YouTube Music su macOS.
-   `test_cookie.py`: Uno script di utilità per verificare se l'autenticazione di YouTube Music (`headers_auth.json`) funziona correttamente.
-   `.gitignore`: Assicura che i file sensibili (`headers_auth.json`, `spotify_credentials.txt`) non vengano caricati su Git.
-   `spotify_credentials.txt.template`: Modello per il file di credenziali di Spotify.