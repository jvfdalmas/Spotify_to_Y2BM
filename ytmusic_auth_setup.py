from ytmusicapi import YTMusic
import os
import sys # <-- AGGIUNGI QUESTA RIGA

# <-- AGGIUNGI QUESTE RIGHE PER IL DEBUG
print(f"DEBUG: Eseguibile Python: {sys.executable}")
print(f"DEBUG: sys.path (percorsi di ricerca moduli):")
for p in sys.path:
    print(f"  - {p}")
try:
    import ytmusicapi
    print(f"DEBUG: ytmusicapi importato da: {ytmusicapi.__file__}")
    print(f"DEBUG: ytmusicapi versione: {ytmusicapi.__version__}")
except Exception as e:
    print(f"DEBUG: Impossibile importare ytmusicapi o ottenere le sue informazioni: {e}")
# <-- FINE RIGHE DI DEBUG

# Questo è il nome del file dove verranno salvate le credenziali
AUTH_FILE = "headers_auth.json"

# ... (il resto del tuo script rimane invariato) ...from ytmusicapi import YTMusic
import os

# Questo è il file dove verranno salvate le credenziali
AUTH_FILE = "headers_auth.json"

# Se il file esiste già, puoi eliminarlo per ricominciare
if os.path.exists(AUTH_FILE):
    os.remove(AUTH_FILE)
    print(f"File '{AUTH_FILE}' esistente rimosso.")

# La funzione setup() ti guiderà attraverso il processo
# Ti chiederà di incollare il tuo cookie string.
print(f"Preparazione all'autenticazione di YouTube Music. Il file '{AUTH_FILE}' verrà creato.")
print("Per favore, segui le istruzioni per ottenere il tuo cookie string da YouTube Music.")
print("Normalmente, devi andare su YouTube Music nel tuo browser, aprire gli strumenti per sviluppatori (F12),")
print("andare su 'Network', ricaricare la pagina e trovare una richiesta che invia un cookie.")
print("Copia l'intero valore del campo 'cookie' dalla richiesta e incollalo qui quando richiesto.")
print("\nPremere Invio per iniziare...")
input() # Attendi che l'utente sia pronto

try:
    # Usa il metodo setup per creare il file di autenticazione
    # Questo metodo è interattivo e ti chiederà il cookie
    YTMusic.setup(filepath=AUTH_FILE, headers_raw=True)
    print(f"✅ File di autenticazione '{AUTH_FILE}' generato con successo.")
except Exception as e:
    print(f"❌ Errore durante la generazione del file di autenticazione: {e}")
