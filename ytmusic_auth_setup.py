from ytmusicapi import YTMusic
import os

# Questo è il file dove verranno salvate le credenziali
AUTH_FILE = "headers_auth.json"

# Se il file esiste già, puoi eliminarlo per ricominciare
if os.path.exists(AUTH_FILE):
    os.remove(AUTH_FILE)
    print(f"File '{AUTH_FILE}' esistente rimosso.")

# Questo script deve essere eseguito solo una volta per generare il file di autenticazione.
print(f"Preparazione all'autenticazione di YouTube Music. Il file '{AUTH_FILE}' verrà creato.")
print("\n--- ISTRUZIONI DETTAGLIATE ---")
print("1. Apri YouTube Music nel tuo browser (es. Chrome, Firefox).")
print("2. Apri gli Strumenti per sviluppatori (premi F12 o Ctrl+Shift+I).")
print("3. Vai alla scheda 'Network' (o 'Rete').")
print("4. Ricarica la pagina di YouTube Music (premi F5 o il pulsante di ricarica).")
print("5. Nella lista delle richieste di rete, cerca una richiesta chiamata 'browse'. Cliccaci sopra.")
print("6. Nella nuova finestra, vai alla sezione 'Headers' (o 'Intestazioni').")
print("7. Scorri verso il basso fino a 'Request Headers' e trova la riga 'cookie'.")
print("8. Copia l'INTERO valore del campo 'cookie' (è una stringa molto lunga).")
print("9. Incolla il valore qui sotto quando richiesto.")
print("\n   NOTA: La stringa del cookie è molto lunga. Quando la incolli nel terminale,")
print("   potrebbe non essere visualizzata completamente. È normale, premi Invio comunque.")
print("\nPremi Invio per continuare e incollare il cookie quando richiesto...")
input() # Attendi che l'utente sia pronto

try:
    # Usa il metodo setup per creare il file di autenticazione
    # Questo metodo è interattivo e ti chiederà il cookie
    YTMusic.setup(filepath=AUTH_FILE, headers_raw=True)
    print(f"✅ File di autenticazione '{AUTH_FILE}' generato con successo.")
except Exception as e:
    print(f"❌ Errore durante la generazione del file di autenticazione: {e}")