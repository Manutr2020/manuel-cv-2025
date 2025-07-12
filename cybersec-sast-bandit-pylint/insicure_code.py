import pickle  # B301: Uso di pickle (rischio di Remote Code Execution)
import hashlib  # B303: Uso di md5, algoritmo crittograficamente debole

# B105: Password hardcoded nel codice
PASSWORD = "SuperSecret123!"

def hash_password(password):
    # B303: Uso di MD5 per hashing delle password (insicuro)
    return hashlib.md5(password.encode()).hexdigest()

# Funzione per simulare l'elaborazione di un testo nelle Digital Humanities
def process_text(text):
    """
    Processa un testo e permette di eseguire codice dinamico (vulnerabile a RCE)
    """
    assert len(text) > 0, "Il testo non può essere vuoto!"  # B101: Uso di assert - serve a verificare la condizione
    
    local_vars = {}  # Dizionario per catturare variabili create in exec()
    exec("result = text[::-1]", {}, local_vars)  # Definisce `result` in local_vars - exec esegue in automatico
    return local_vars["result"]  # Recupera `result`

# Funzione per serializzare i dati (vulnerabile a deserializzazione non sicura)
def save_data(data, filename):
    with open(filename, 'wb') as f:   #'wb' significa write binary
        pickle.dump(data, f)  # B301: Uso di pickle (rischio di Remote Code Execution) - pickle serve a convertire un oggetto in formato binario e metterlo su file

def load_data(filename):
    with open(filename, 'rb') as f:    #'rb' significa read binary
        return pickle.load(f)  # B301: Possibile exploit con payload malevolo - Legge un file contenente dati serializzati e ricostruisce l'oggetto originale.

# Simulazione di un input utente per l'esecuzione dinamica
user_input = input("Inserisci un comando Python: ")  # L'utente inserisce il codice
exec(user_input)    # B102: Uso di exec per eseguire codice arbitrario - RCE (remote code execution) e non solo remote

# Esempio di uso delle funzioni
if __name__ == "__main__":         #ciò avviene solo se questo codice non viene eseguito direttamente e non importato come modulo 
    testo = "Questo è un esempio di Digital Humanities con vulnerabilità."
    testo_processato = process_text(testo)
    print("Testo processato:", testo_processato)

    # Simuliamo il salvataggio di dati in un file
    data = {"username": "admin", "password": PASSWORD}
    save_data(data, "dati.pkl")

    # Carichiamo i dati salvati
    dati_caricati = load_data("dati.pkl")
    print("Dati caricati:", dati_caricati)

    # Hash della password (insicuro!)
    print("Hash della password (MD5, insicuro):", hash_password(PASSWORD))