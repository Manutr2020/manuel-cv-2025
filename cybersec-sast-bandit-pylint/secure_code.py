import json
import hashlib
import os

PASSWORD = os.getenv("MY_SECRET_PASSWORD", "default_password")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def process_text(text):
    if len(text) == 0:
        raise ValueError("Il testo non può essere vuoto!")
    return text[::-1]

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    testo_processato = process_text("Questo è un esempio di Digital Humanities con sicurezza migliorata.")
    print("Testo processato:", testo_processato)

    save_data({"username": "admin", "password": PASSWORD}, "dati.json")
    print("Dati caricati:", load_data("dati.json"))

    print("Hash della password (SHA-256, sicuro):", hash_password(PASSWORD))
