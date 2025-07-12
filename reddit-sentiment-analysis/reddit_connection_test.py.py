import praw
import os

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Controllo credenziali
if not all([reddit.client_id, reddit.client_secret, reddit.user_agent]):
    raise ValueError("Variabili d'ambiente mancanti: controlla REDDIT_CLIENT_ID, SECRET, AGENT")

try:
    subreddit = reddit.subreddit('italia')
    print(f"Connessione riuscita! Subreddit: {subreddit.display_name}")
except Exception as e:
    print(f"Errore di connessione: {e}")