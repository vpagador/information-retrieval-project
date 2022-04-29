import pandas as pd
import json
import nltk
from nltk.corpus import stopwords
import re

df = pd.read_json("publications.json")
doc_list = list(df['title'])

# building the inverted indexer MODIFIED WITHOUT STOPWORDS AND WITH/WITHOUT HYTHENS (words are counted then split  further)
filter_ = "(,),<,>,+"
dash = '-'
inverted_index = {}

sw = stopwords.words('english') + ['&'] + ['A']

for i, doc in enumerate(doc_list):
    for term in doc.split():
        # put them all as lower case and put through filter_
        term = term.lower().translate({ord(i): None for i in filter_})
        # if not a dash-word
        if dash not in term and term not in sw:
            if term in inverted_index:
                inverted_index[term].append(i)
            else:
                inverted_index[term] = [i]
        # if a dash-word
        elif term not in sw:
            if term in inverted_index:
                inverted_index[term].append(i)
            else:
                inverted_index[term] = [i]
            # split the term into multiple terms
            out = re.split(r'-', term)
            for word in out:
                word = word.lower()
                if word in inverted_index:
                    inverted_index[word].append(i)
                else:
                    inverted_index[word] = [i]


with open('index.json', 'w') as outfile:
    json.dump(inverted_index, outfile)
