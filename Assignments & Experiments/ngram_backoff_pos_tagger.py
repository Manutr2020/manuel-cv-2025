import random
import nltk
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

# STEP 4: tagger in isolation
default_tagger = nltk.DefaultTagger("NOUN")
unigram_tagger = nltk.UnigramTagger(train_sents)
bigram_tagger = nltk.BigramTagger(train_sents)
trigram_tagger = nltk.TrigramTagger(train_sents)

print("Taggers in isolation:")
print("Default tagger accuracy:", default_tagger.accuracy(test_sents))
print("Unigram tagger accuracy:", unigram_tagger.accuracy(test_sents))
print("Bigram tagger accuracy:", bigram_tagger.accuracy(test_sents))
print("Trigram tagger accuracy:", trigram_tagger.accuracy(test_sents))

#STEP 5: taggers with backoff
unigram_tagger_bo = nltk.UnigramTagger(train_sents, backoff=default_tagger)
bigram_tagger_bo = nltk.BigramTagger(train_sents, backoff=unigram_tagger_bo)
trigram_tagger_bo = nltk.TrigramTagger(train_sents, backoff=bigram_tagger_bo)

print("\nTaggers with backoff:")
print("Unigram tagger with backoff accuracy:", unigram_tagger_bo.accuracy(test_sents))
print("Bigram tagger with backoff accuracy:", bigram_tagger_bo.accuracy(test_sents))
print("Trigram tagger with backoff accuracy:", trigram_tagger_bo.accuracy(test_sents))

#STEP 6: taggers with backoff and non-zero cutoff
unigram_cut_2 = nltk.UnigramTagger(train_sents, backoff=default_tagger, cutoff=2)
bigram_cut_2 = nltk.BigramTagger(train_sents, backoff=unigram_cut_2, cutoff=2)
trigram_cut_2 = nltk.TrigramTagger(train_sents, backoff=bigram_cut_2, cutoff=2)

unigram_cut_3 = nltk.UnigramTagger(train_sents, backoff=default_tagger, cutoff=3)
bigram_cut_3 = nltk.BigramTagger(train_sents, backoff=unigram_cut_3, cutoff=3)
trigram_cut_3 = nltk.TrigramTagger(train_sents, backoff=bigram_cut_3, cutoff=3)

print("\nTaggers with backoff and cutoff:")
print("Unigram backoff cutoff=2 accuracy:", unigram_cut_2.accuracy(test_sents))
print("Bigram backoff cutoff=2 accuracy:", bigram_cut_2.accuracy(test_sents))
print("Trigram backoff cutoff=2 accuracy:", trigram_cut_2.accuracy(test_sents))

print("Unigram backoff cutoff=3 accuracy:", unigram_cut_3.accuracy(test_sents))
print("Bigram backoff cutoff=3 accuracy:", bigram_cut_3.accuracy(test_sents))
print("Trigram backoff cutoff=3 accuracy:", trigram_cut_3.accuracy(test_sents))

#STEP 7: comments
'''
The results vary slightly across runs due to the random split of training and test data,
but some clear patterns can be observed.

The default tagger performs poorly, with accuracy around 0.27–0.29, as it assigns the
same tag to all words. The unigram tagger performs much better (around 0.75–0.77),
since it learns the most frequent tag for each word.

The bigram and trigram taggers in isolation perform worse (around 0.14 and 0.09),
due to data sparsity: many n-grams in the test set are not seen during training.

Backoff significantly improves performance. The best results are achieved by bigram
or trigram taggers with backoff, reaching around 0.87–0.88 accuracy. For example,
the bigram backoff tagger reached about 0.88 in one run.

Using a non-zero cutoff reduces accuracy (around 0.79–0.82), since rare but useful
patterns are removed.

The best performing model is the bigram tagger with backoff,
which consistently achieved the highest accuracy (~0.88).
'''

#STEP 8: 5 sentences of my best tagger

print("\nFive sentences tagged by the best tagger (bigram backoff):\n")

for i, test_sent in enumerate(test_sents[:5]):
    print(f"SENTENCE #{i+1}:",
          " ".join(nltk.tag.tuple2str(wt)
                   for wt in bigram_tagger_bo.tag(nltk.untag(test_sent))))
    print()

#STEP 9:

'''
The best tagger in this assignment, the bigram tagger with backoff, performs
clearly better than the sequential Naive Bayes POS tagger from Workshop exercise 3.1.
The Naive Bayes tagger reached about 0.70 accuracy, while the best backoff bigram
tagger reached about 0.88.

This is not surprising. 
it uses local context when possible, and falls back to simpler models when needed.
Because of this, it is more robust than the Naive Bayes tagger used in exercise 3.1.
'''