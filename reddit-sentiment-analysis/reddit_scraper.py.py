import praw
import json
import time
import os
import datetime

# Configurazione dell'API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Controllo credenziali
if not all([reddit.client_id, reddit.client_secret, reddit.user_agent]):
    raise ValueError("Variabili d'ambiente mancanti: controlla REDDIT_CLIENT_ID, SECRET, AGENT")

# Lista per contenere i dati
data = []

# Nome del subreddit
subreddit_name = 'TeenagersITA'
subreddit = reddit.subreddit(subreddit_name)

# Estrazione dei dati
try:
    for post in subreddit.new(limit=4):  # Limite massimo di 10 post
        if post.is_self:
            try:
                # Assicurati che il titolo e il contenuto siano presenti
                titolo = post.title.strip() if post.title else "Titolo non disponibile"
                testo = post.selftext.strip() if post.selftext else "Testo non disponibile"

                # Aggiungi il post come elemento
                data.append({
                    "tipo": "post",
                    "contenuto": f"Titolo: {titolo}\n\n{testo}"
                })

                # Recupera un massimo di 5 commenti non rimossi/eliminati
                post.comments.replace_more(limit=0)  # Rimuovi i placeholder dei commenti
                count = 0
                for comment in post.comments:
                    if comment.body.strip() and comment.body != "[removed]" and comment.body != "[deleted]":
                        data.append({
                            "tipo": "commento",
                            "contenuto": comment.body.strip()
                        })
                        count += 1
                    if count >= 7:  # Ferma dopo 5 commenti
                        break

                # Rispetta i limiti dell'API
                time.sleep(1)

            except Exception as e:
                print(f"Errore durante l'elaborazione del post: {e}")
except Exception as e:
    print(f"Errore durante l'estrazione dei dati: {e}")

# Creazione della cartella di output
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Nome del file con timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f'{output_folder}/reddit_data_{subreddit_name}_{timestamp}.json'

# Salva i dati in JSON
try:
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"I dati sono stati salvati in '{output_file}'")
except Exception as e:
    print(f"Errore durante il salvataggio del file JSON: {e}")