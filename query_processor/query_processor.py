import json
import pandas as pd

# Open inverted index
with open('index.json', 'r') as f:
    index = json.load(f)

# Open documents (list of crawled articles) with pandas
df = pd.read_json('publications.json')


def query_processor():
    results = []
    query = input('search: ')
    # if there are more than 1 term in the query, put a hypthen in the spaces
    # search documents with the hypthen(ed) terms using indexer
    if len(query.split()) > 1:
        lower_term_dashed = query.lower().replace(' ', '-')
        # if term exists in index
        if lower_term_dashed in index.keys():
            for docs in index[lower_term_dashed]:
                if docs not in results:
                    results.append(docs)

    # split query into terms and search documents using indexer
    for input_terms in query.split():
        lower_term = input_terms.lower()
        # if term exists in index
        if lower_term in index.keys():
            for docs in index[lower_term]:
                if docs not in results:
                    results.append(docs)
        else:
            return print(f'''No Results Available for: {lower_term}''')

    # print all results
    number_of_results = 0
    for i,docs in enumerate (results):
        print(f'''\nresult number: {i+1}\n{df.transpose()[docs]}\n''')
        number_of_results +=1 
    
    print('results obtained: ', number_of_results,'\n')

    return 0


