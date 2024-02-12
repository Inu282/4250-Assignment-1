#-------------------------------------------------------------------------
# AUTHOR: Alvin Le
# FILENAME: A1.py
# SPECIFICATION: Calculating and printing out a TF-IDF Matrix
# FOR: CS 4250- Assignment #1
# TIME SPENT: 2-3 hours
#-----------------------------------------------------------*/
import csv
import math

# Reading the data from a CSV file
documents = []
with open('collection.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append(row[0].split())

# Stopwords removal
stopwords = set(['I','and','She','her','They','their'])
documents = [[word for word in document if word not in stopwords] for document in documents]

# Stemming
stemming = {'cats': 'cat', 'loves': 'love', 'dogs': 'dog'} 
documents = [[stemming.get(word, word) for word in document] for document in documents]

# Identifying the index terms
terms = list(set(word for document in documents for word in document))

# Building the document-term matrix by using the tf-idf weights
# Calculate IDF
N = len(documents)
idf = [0] * len(terms)
for i, term in enumerate(terms):
    df = sum(1 for document in documents if term in document)
    idf[i] = math.log10(N / df)

# Calculate TF-IDF for each document
docTermMatrix = []
for document in documents:
    # Calculate TF for the document
    tf = [document.count(term) / len(document) for term in terms]
    # Calculate TF-IDF for the document
    tfidf = [tf[i] * idf[i] for i in range(len(terms))]
    docTermMatrix.append(tfidf)

# Printing the document-term matrix 
for i, row in enumerate(docTermMatrix):
    print(f"Document {i+1} TF-IDF:")
    for j, term in enumerate(terms):
        if term not in stopwords:
            print(f"\tTerm '{term}': {row[j]}")
