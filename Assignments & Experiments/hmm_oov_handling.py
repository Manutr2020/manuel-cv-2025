import random
import nltk
from nltk.tag import hmm
import sys

def read_tagged_sents(filepath):
    """ This method reads the file at self.__filepath and extracts
    all the tagged sentences from the file (for evaluation purposes).
    The return value of this method consists of a list of
    lists. On the highest level, we have a list of
    sentences. Then, every sentence consists of a list of
    tuples. Every tuple is a pair of a word and its POS
    tag.

    Example snippet of the data structure that is returned:
    [[('Kävelyreitti', 'NOUN'), ('III', 'ADJ')], [('Jäällä',
    'NOUN'), ('kävely', 'NOUN'), ('avaa', 'VERB'), ('aina',
    'ADV'), ('hauskoja', 'ADJ'), ('ja', 'CONJ'), ('erikoisia',
    'ADJ'), ('näkökulmia', 'NOUN'), ('kaupunkiin', 'NOUN'), ('.',
    'PUNCT')], [('Vähän', 'ADV'), ('samanlainen', 'ADJ'),
    ('tunne', 'NOUN'), ('kuin', 'SCONJ'), ...] ... ]

    Don't change anything here.
    """
    tagged_sents = []
    try:
        # When we open a file with "with", the file is always cleanly closed as well
        with open(filepath, "r", encoding="UTF-8") as gs_file:
            line = gs_file.readline()
            while line != "":
                tagged_sents.append([(w.lower(), t) for w,t in [nltk.tag.str2tuple(wt) for wt in line.split()]])
                line = gs_file.readline()
    except OSError:
        print("Error reading file.")
        sys.exit()
    return tagged_sents

tagged_sents = read_tagged_sents("fi-ud-train.pos-tagged.txt")
random.shuffle(tagged_sents)
train_sents, test_sents = tagged_sents[500:], tagged_sents[:500]


#STEP 3
word_counts = {}
for sent in train_sents:
    for w, _ in sent:
        word_counts[w] = word_counts.get(w, 0) + 1

train_sents = [[(("<UNK>", t) if word_counts[w] == 1 else (w, t)) for w, t in sent]
               for sent in train_sents]

train_vocab = set(w for sent in train_sents for (w, t) in sent)

# STEP 2
total_words = sum(len(sent) for sent in test_sents)
unk_count = sum(
    1 for sent in test_sents for (w, _) in sent if w not in train_vocab
)

print("Relative frequency of OOV words:", unk_count / total_words)

# STEP 1
test_sents_unk = [
    [(w if w in train_vocab else "<UNK>", t) for (w, t) in sent]
    for sent in test_sents
]

print("Relative frequency of OOV words:", unk_count / total_words)

#STEP 5
trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_sents)

print("accuracy:", tagger.accuracy(test_sents_unk))

#STEP 6
test_words_unk = [[w for (w, t) in sent] for sent in test_sents_unk]
tagged_test = [tagger.tag(sent) for sent in test_words_unk]

for o, u, p in zip(test_sents[:5], test_sents_unk[:5], tagged_test[:5]):
    print(" ".join(
        f"{(ow + '<UNK>' if uw == '<UNK>' else ow)}/{pt}"
        for (ow, _), (uw, _), (_, pt) in zip(o, u, p)
    ))

#STEP 7
'''
The results with <UNK> are clearly better than before. In the previous version
without <UNK>, the accuracy was only around 0.32–0.37, and many unknown words
were tagged incorrectly, often defaulting to the same tags such as VERB or PRON.
After introducing <UNK>, the accuracy improves to about 0.83–0.84. The tagger
still makes mistakes with out-of-vocabulary words, especially confusing NOUN,
VERB, ADJ, and PROPN, but overall the predictions are much more reasonable and stable.
'''
