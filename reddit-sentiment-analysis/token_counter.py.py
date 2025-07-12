import json
from nltk.tokenize import word_tokenize
import nltk
import os

# Scarica i dati necessari per nltk (esegui solo la prima volta)
nltk.download('punkt')

def count_tokens_from_json(file_path):
    try:
        # Verifica che il file esista
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Il file non esiste nel percorso: {file_path}")
        
        # Leggi il file JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Carica il contenuto JSON
            print("Il file JSON è stato caricato correttamente.")
        
        # Controlla se il file è una lista di oggetti
        if not isinstance(data, list):
            raise ValueError("Il file JSON non contiene una lista come struttura principale.")

        total_tokens = 0

        # Conta i token nel campo 'contenuto'
        for idx, item in enumerate(data):
            contenuto = item.get("contenuto", "")
            tokens = word_tokenize(contenuto)
            total_tokens += len(tokens)
            print(f"Oggetto {idx+1}: {len(tokens)} token trovati.")

        print(f"Il file contiene un totale di {total_tokens} token.")
        return total_tokens

    except json.JSONDecodeError as jde:
        print(f"Errore nel decodificare il file JSON: {jde}")
    except FileNotFoundError as fnf:
        print(fnf)
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

# Percorso del file JSON
file_path = "data/reddit_data.json"
count_tokens_from_json(file_path)

