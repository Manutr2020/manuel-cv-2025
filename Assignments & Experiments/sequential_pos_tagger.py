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
'''
print(tagged_sents[:2])
'''
random.shuffle(tagged_sents)
'''
print("after shuffle", tagged_sents[:3])
'''
train_sents, test_sents = tagged_sents[500:], tagged_sents[:500]
'''
print("the number of sentences in training set:", len(train_sents))
print("the number of sentences in test set:", len(test_sents))
'''

#STEP 4
# and modification for step 8
def pos_features(sentence, i, history): 
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
        features["prev-prev-word"] = "<START>"
        features["prev-prev-tag"] = "<START>" 

    elif i == 1:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
        features["prev-prev-word"] = "<START>"
        features["prev-prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
        features["prev-prev-word"] = sentence[i-2]
        features["prev-prev-tag"] = history[i-2] 
    return features       

class ConsecutivePosTagger(nltk.TaggerI): 

    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history) #return the words with their tag

    def tag_and_get_features(self, sentence):
        features = []
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
            features.append(featureset)
        return zip(sentence, features) # return the words with their features

#STEP 5
tagger = ConsecutivePosTagger(train_sents)
print("accuracy on the test set", tagger.accuracy(test_sents))

print(list(tagger.tag(["olen", "turussa", "."])))

#STEP 6 - 7
print("print 5 tagged sentences and also the features of the words in the sentences")

for i, test_sent in enumerate(test_sents[:5]):
    print(f"SENTENCE #{i+1}:",
           " ".join(nltk.tag.tuple2str(wt) for wt in tagger.tag(nltk.untag(test_sent))))
    for word, features in tagger.tag_and_get_features(nltk.untag(test_sent)):
        print(f"     {word};  {features}")
    print()
    
#STEP 8  
'''
After adding additional contextual features (prev-prev-word and prev-prev-tag),
the performance of the ConsecutivePosTagger remained approximately the same.
'''


#STEP 9
'''
The ConsecutivePosTagger performs clearly better than the regular-expression
based POS tagger (about 0.69 vs 0.46 accuracy). This is because it learns from
data and uses contextual features (such as previous words and tags), while the
regexp tagger relies only on fixed word-form patterns (and on my lack of knowledge of the finnish language).

However, the results are not directly fully comparable, because the evaluation
methods differ: the regexp tagger is evaluated on the whole dataset, while the
Naive Bayes tagger is trained on a subset and tested on a separate subset.
In addition, the random split causes small variations in the results.
'''



