import csv
import json
from collections import Counter
import spacy

# Carica il modello di Spacy per l'italiano
nlp = spacy.load("it_core_news_sm")

# Funzione per contare i token e i type in una stringa di testo
def count_tokens_and_types(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_punct and not token.is_space]
    types = set(tokens)
    return len(tokens), len(types)

# Funzione per estrarre le etichettature da una stringa JSON
def extract_labels(json_str):
    labels = []
    if json_str:
        try:
            annotations = json.loads(json_str.replace("'", '"'))
            for annotation in annotations:
                labels.extend(annotation.get("labels", []))
        except json.JSONDecodeError:
            pass  # Ignora errori di parsing
    return labels

# Lettura del file CSV
file_path = "data/prog_evan.csv"   # Sostituisci con il percorso al file CSV

total_tokens = 0
total_types = 0
total_labels = 0
label_counter = Counter()

with open(file_path, "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        contenuto = row["contenuto"]
        emotion_labels = row["emotion_labels"]

        # Conta i token e i type
        tokens, types = count_tokens_and_types(contenuto)
        total_tokens += tokens
        total_types += types

        # Estrai e conta le etichette
        labels = extract_labels(emotion_labels)
        total_labels += len(labels)
        label_counter.update(labels)

# Stampa i risultati
print(f"Numero totale di token: {total_tokens}")
print(f"Numero totale di type: {total_types}")
print(f"Numero totale di etichettature: {total_labels}")
print("Numero di etichettature per label:")
for label, count in label_counter.items():
    print(f"- {label}: {count}")
