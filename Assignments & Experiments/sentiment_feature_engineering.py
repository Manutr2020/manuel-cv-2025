import nltk
from nltk.corpus import movie_reviews
import random
from nltk import bigrams

documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = [w for w, f in all_words.most_common(1000)]

all_bigrams = nltk.FreqDist(
    bigram 
    for bigram in bigrams(w.lower() for w in movie_reviews.words())
)
bigrams_features = [bg for bg, f in all_bigrams.most_common(1000)]

def contains_features(document): 
    document_words = set(w.lower() for w in document) 
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

def begins_features(document):
    first_words = set(w.lower() for w in document[:30])
    features = {}
    for word in word_features:
        features[f'begins({word})'] = (word in first_words)
    return features

def ends_features(document):
    last_words = set(w.lower() for w in document[-30:])
    features = {}
    for word in word_features:
        features[f'ends({word})'] = (word in last_words)
    return features

def bigram_features(document):
    bigrams_document = set(bigrams(w.lower() for w in document))
    features = {}
    for w1, w2 in bigrams_features:
        features[f'bigram({w1} {w2})'] = ((w1, w2) in bigrams_document)
    return features


def combined_features(document):
    features = {}
    features.update(contains_features(document)) # update() merges dictionaries
    features.update(begins_features(document))
    features.update(ends_features(document))
    features.update(bigram_features(document))
    return features

def evaluate_feature_extractor(feature_function):
    featuresets = [(feature_function(d), c) for (d, c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]

    classifier = nltk.NaiveBayesClassifier.train(train_set)

    gold = [c for (f, c) in test_set]
    test = classifier.classify_many([f for (f, c) in test_set])

    cm = nltk.ConfusionMatrix(gold, test)
    print(cm)

evaluate_feature_extractor(combined_features)

'''
    |  n  p |
    |  e  o |
    |  g  s |
----+-------+
neg |<44>15 |
pos | 14<27>|
----+-------+
(row = reference; col = test)
'''

'''
The value in the lower left corner is the number of positive reviews
that were incorrectly classified as negative.
--> These are false negatives.
'''