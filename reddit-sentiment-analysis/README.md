# Analisi delle Emozioni su Reddit

Questo progetto analizza i contenuti testuali di Reddit (post e commenti) per identificarne l’emozione prevalente, usando le 8 emozioni base del modello di Plutchik.  
Il lavoro combina scraping, annotazione manuale e analisi dei dati, con strumenti come Python e Label Studio.

---

## 📁 Struttura del progetto

- `reddit_scraper.py` – Script per scaricare post/commenti da Reddit.
- `token_counter.py` – Conta i token nei testi.
- `annotation_stats.py` – Statistiche sulle annotazioni fatte.
- `labeling_interface/` – Contiene l’interfaccia XML per Label Studio.
- `output/` – Contiene i dati testuali scaricati da Reddit.
- `.env.example` – Variabili d’ambiente (client ID, secret, ecc.) da impostare.

---

## ⚙️ Come usare Label Studio

Per replicare l’ambiente di annotazione:

1. Installa Label Studio (se non lo hai già):

   ```bash
   pip install label-studio
